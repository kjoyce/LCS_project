import Scientific.IO.NetCDF as nc
import sys
import os
import re
import numpy as np
from mpl_toolkits.basemap import Basemap
import  matplotlib.pyplot as plt
from datetime import datetime,timedelta,tzinfo
from IPython.Debugger import Tracer; debug_here = Tracer()

class NcomTime(datetime):
  def __new__(cls,hrs):
    d = timedelta(hours=hrs)
    t0=datetime(2000,1,1,0,0,0)
    return d + t0

class NcomNetcdf:
  def __init__(self,infilename):
    if os.path.isdir(infilename):
# Change this to read new input type
#      self.import_txt(infilename)
#      [self.x,self.y] = [np.zeros( (len(self.t), self.lon.shape[1], self.lon.shape[2]) )]*2
#      for i in range(len(self.t)):
#	self.x[i],self.y[i] = stereo_proj(self.lon[i],self.lat[i])
      self.dirname = infilename
      pass
    else:
      self.infile = nc.NetCDFFile(infilename,'r')
      self.dirname = infilename[0:-3]

  def set_time_range(self,tmin=None,tmax=None):
    if( tmin is None ): 
      tmin = self.infile.variables['time'][0];
    if( tmax is None ):
      tmax = self.infile.variables['time'][-1];
    
    # quick find closest neighbor 
    idx0 = 0
    while( self.infile.variables['time'][idx0] > tmin ):
      idx0 += 1

    idx1 = 0
    while( self.infile.variables['time'][idx1-1] < tmax ):
      idx1 -= 1
    
    if (idx0 == idx1): #then both are zero
      self.t = self.infile.variables['time'][:]
    else:
      self.t = self.infile.variables['time'][idx0:idx1]
    
  def set_grid_region( self,lat_min = 45, lat_max = 70, lon_min = -170, lon_max = -120 ):
    X = self.infile.variables['lon'].getValue()
    Y = self.infile.variables['lat'].getValue()

# assuming uniform grid
    deltax = abs(X[-1] - X[0]) / X.shape[0] 
    deltay = abs(Y[-1] - Y[0]) / Y.shape[0]

# These particular files measure latitude using spherical coordinates
# i.e. 0 (South Pole) to 180 (North Pole).
# The initial latitude is not zero (due to Antarctica) and have only
    x0 = int(abs(360+lon_min - X[0])/deltax)
    x1 = int(abs(360+lon_max - X[0])/deltax)
    y0 = int(abs(lat_min - Y[0])/deltay)
    y1 = int(abs(lat_max - Y[0])/deltay)
    self.min_lon = x0
    self.max_lon = x1
    self.min_lat = y0
    self.max_lat = y1
    self.lon = X[x0:x1]
    self.lat = Y[y0:y1]

    self.__set_stere_basemap()


  def load_memory(self):
    if not( 't' in dir(self) ):
      raise NetCdfPreprocessorError("Must preload time variables")
    if not( 'lon' in dir(self) and 'lat' in dir(self) ):
      raise NetCdfPreprocessorError("Must preload lon and lat variables")

    x0 = self.min_lon
    x1 = self.max_lon
    y0 = self.min_lat
    y1 = self.max_lat

    Tlen = self.infile.variables['water_u'].shape[0]
    self.u = np.zeros( (Tlen,(y1-y0),(x1-x0)))
    self.v = np.zeros( (Tlen,(y1-y0),(x1-x0)))
    for t in range(Tlen):
      self.u[t] = self.infile.variables['water_u'][t][0][y0:y1][:,x0:x1]
      self.v[t] = self.infile.variables['water_v'][t][0][y0:y1][:,x0:x1]
      
    
  def interpolate_grid(self,res):
    from scipy.interpolate import griddata
    # make a structured grid
    xmin = self.x[0][0]
    xmax = self.x[0][-1]
    ymin = self.y[0][self.y.shape[1]/2]
    ymax = self.y[-1][0]

    grid_x,grid_y = np.mgrid[xmin:xmax:round(self.x.shape[0]*res)*1j,ymin:ymax:round(self.x.shape[1]*res)*1j]
    self.grid_x = grid_x
    self.grid_y = grid_y
    x = self.x.reshape(self.x.shape[0]*self.x.shape[1])
    y = self.y.reshape(self.y.shape[0]*self.y.shape[1])
    u = self.u.reshape(25,(self.y.shape[0]*self.y.shape[1])) 
    v = self.u.reshape(25,(self.y.shape[0]*self.y.shape[1])) 

    self.ui = np.zeros( (self.u.shape[0], grid_x.shape[0], grid_x.shape[1]))
    self.vi = np.zeros( (self.u.shape[0], grid_x.shape[0], grid_x.shape[1]))
    for i in range( u.shape[0] ):
      self.ui[i] = griddata((x,y),u[i],(grid_x,grid_y),method='linear')
      self.vi[i] = griddata((x,y),v[i],(grid_x,grid_y),method='linear')

  
  def __set_stere_basemap(self):
# Here we use spherical stereographic projection to estimate
# the width and height for the more precise stereographic
# projection given in the Basemap libraries
# 
# The projection is from the south pole to minimize distortion.  R is the
# approximate radius of the earth.  The image of a geodesic square on a
# sphere under stereographic projection is a closed region bounded by two
# arcs of circles and two diagonal lines.  
#
#     /`-_-'\
#    /       \
#    `-_   _-'
#       `-'
#
# Hence if x,y are the returned coordinates from stereo graphic
# projection, then the box bounding the region is from x[-1][0] to x[-1][-1]
# and y[0][0] to y[-1][midpoint]

# estimating the desired width 
    x,y = stereo_proj(self.lon,-self.lat) 
    wd = abs(x[0][0] - x[0][-1])
    ymid0 = (y[0][ y.shape[1]/2 ] + y[0][ y.shape[1]/2 +1 ])/2
    ymid1 = (y[-1][ y.shape[1]/2 ] + y[-1][ y.shape[1]/2 +1 ])/2
    ht = abs(ymid1 - ymid0)

    self.basemap = Basemap(projection = 'stere',
		 lon_0 = .5*( self.lon[0] + self.lon[-1]),
		 lat_0 = .5*( self.lat[0] + self.lat[-1]),
		 width=wd,
		 height=ht)

#Basemap(projection='stere',lon_0=.5*(lon[0]+lon[-1]),lat_0=.5*(l
#at[0]+lat[-1]),llcrnrlon=lon[0],llcrnrlat=lat[0],urcrnrlon=lon[-1],urcrnrlat=l
#at[-1])
    
    self.x,self.y = self.basemap(*np.meshgrid(self.lon,self.lat))
    debug_here()

  def get_time_readable(self):
    T = self.infile.variables['time'].getValue()
    return [NcomTime(int(x)) for x in T]
  
  def export_stereo_txt(self):
    try:
      os.mkdir(self.dirname+"stereo")
    except OSError:
      pass

    fT = self.get_time_readable()
    for t in range(len(fT)):
      outfilename = self.dirname + "/ncom_" + fT[t].strftime("%Y%m%d%H%M") + ".txt"
      outfile = open(outfilename,'w')
      for i in range(self.grid_x.shape[0]):
	for j in range(self.grid_x.shape[1]):
	  outfile.write( "%f,%f,%f,%f\n" % (self.grid_x[i][j],self.grid_y[i][j],self.ui[t][i][j],self.vi[t][i][j]))
      outfile.close()
    return 1

  def export_spherical_txt(self):
    try:
      os.mkdir(self.dirname+"stereo")
    except OSError:
      pass

    fT = self.get_time_readable()
    for t in range(len(fT)):
      outfilename = self.dirname + "/ncom_" + fT[t].strftime("%Y%m%d%H%M") + ".txt"
      outfile = open(outfilename,'w')
      for i in range(self.lon.shape[0]):
	for j in range(self.lon.shape[1]):
	  outfile.write( "%f,%f,%f,%f\n" % (self.lon[i][j],self.lat[i][j],self.u[t][i][j],self.v[t][i][j]))
      outfile.close()
    return 1

  def load_frame(self,fdatetime):
    fname = "%s/ncom_%04d%02d%02d%02d%02d.txt" % (self.dirname,fdatetime.year,fdatetime.month,fdatetime.day,fdatetime.hour,fdatetime.minute)

    fh = open(fname)
    d = dict()
    for l in fh:
      [alon,alat,au,av] = l.split(',')
      [alon,alat,au,av] = map(np.float64,[alon,alat,au,av])
# Commented out since no longer need point array
#      if not( np.any(np.isnan((au,av)) )):
#	if 'points' in dir(self): 
#	    self.points.append( (alon,alat,au,av) )
#	else:
#	  self.points = [(alon,alat,au,av)]
#
      if alon in d.keys():
	d[alon].append( (alat,au,av) )
      else:
	d[alon] = [ (alat,au,av) ]
    u = np.zeros( (len(d.keys()), len(d[d.keys()[0]])))
    v = np.zeros( (len(d.keys()), len(d[d.keys()[0]])))
    lon = np.zeros( (len(d.keys()), len(d[d.keys()[0]])))
    lat = np.zeros( (len(d.keys()), len(d[d.keys()[0]])))
    for i in range(len(d.keys())):
      for j in range(len( d[d.keys()[i]][0] )):
	lon[i][j] = d.keys()[i]
	lat[i][j] = d[d.keys()[i]][j][0]
	u[i][j] = d[d.keys()[i]][j][1]
	v[i][j] = d[d.keys()[i]][j][2]
    u = np.array(u)
    v = np.array(v)
    lon = np.array(lon)
    lat = np.array(lat)
    if 'u' in dir(self):
      self.u.append(u)
      self.v.append(v)
      self.lon.append(lon)
      self.lat.append(lat)
    else:
      self.u = [u]
      self.v = [v]
      self.lon = [lon]
      self.lat = [lat]


  def import_txt(self,dirname):
    files = os.listdir(dirname)
    self.points = []
    self.u = []
    self.v = []
    self.lon = []
    self.lat = []
    self.t = []
    for f in files:
      to_match = "^ncom_(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})\.txt$"
      m = re.match(to_match,f)
      self.t.append(datetime(*[int(s) for s in m.groups()]))
      if m:
	fname = "%s/%s" % (dirname,f)
	fh = open(fname )
	d = dict()
	for l in fh:
	  [alon,alat,au,av] = l.split(',')
	  [alon,alat,au,av] = map(np.float64,[alon,alat,au,av])
	  self.points.append( (alon,alat,au,av) )
	  if alon in d.keys():
	    d[alon].append( (alat,au,av) )
	  else:
	    d[alon] = [ (alat,au,av) ]
	[u,v,lon,lat] = [np.zeros( (len(d.keys()), len(d[d.keys()[0]])))]*4
	for i in range(len(d.keys())):
	  for j in range(len( d[d.keys()[i]][0] )):
	    lon[i][j] = d.keys()[i]
	    lat[i][j] = d[d.keys()[i]][j][0]
	    lat[i][j] = d[d.keys()[i]][j][1]
	    lat[i][j] = d[d.keys()[i]][j][2]
	self.u.append(u)
	self.v.append(v)
	self.lon.append(lon)
	self.lat.append(lat)

    self.u = np.array(self.u)
    self.v = np.array(self.v)
    self.lon = np.array(self.lon)
    self.lat = np.array(self.lat)
	
  def export_nc(self):
    netfilename = self.dirname + "_AK_stereo.nc"
    netfile = nc.NetCDFFile(netfilename,'w')
    net_dims = (netfile.createDimension('t',self.u.shape[0]),
		netfile.createDimension('lon',self.u.shape[2]),
		netfile.createDimension('lat',self.u.shape[1]))

    net_u = netfile.createVariable('u','d',('t','lon','lat'))
    net_v = netfile.createVariable('v','d',('t','lon','lat'))
    net_lon = netfile.createVariable('lon','d',('lon',))
    net_lat = netfile.createVariable('lat','d',('lat',))
    net_t = netfile.createVariable('t','d',('t',))

    net_u.assignValue(self.u)
    net_v.assignValue(self.v)
    net_lat.assignValue(self.lat)
    net_lon.assignValue(self.lon)
    net_t.assignValue(self.t)

    return netfile.close();

def stereo_proj(lon,lat):
  from numpy import meshgrid,pi,sin,cos,tan,abs
  R = 6378.1e3
# Rotate to spherical coordinates.  I.e. assuming the longitude coordinates
# are sorted, make it the 0th meridian (which is irrelevant to
# stereographic projection) and measure latitude from the north pole.
  lon = lon - lon[0]
  lat = 90 - lat
  
  if len(lon.shape) == 1:
    lon,lat = meshgrid(lon,lat)
  lat = pi/180*lat
  lon = pi/180*lon
  x = cos( lon ) / tan( lat/2 )
  y = sin( lon ) / tan( lat/2 )
# rotate so that the north pole is upwards
  x,y = rotate_pts(x,y,-(abs(lon[0][0]-lon[-1][-1])/2 + pi/2))
  return R*x,R*y

def dist(x1,x2): 
  return np.sqrt( ( x1[0] - x2[0] )**2 + (x1[1] - x2[1])**2 ) 

def rotate_pts(x,y,th):
  from numpy import sin,cos
  return (x*cos(th) - y*sin(th), x*sin(th) + y*cos(th))

def get_points(x,y,t=[-1]):
  I = x.shape[0]
  J = x.shape[1]
  K = len(t)
  points = [None]*I*J*K
  for k in range(K):
    for i in range(I):
      for j in range(J):
	if len(t) > 1:
	    points[k*I*J + i*J + j] = ( (t[k], x[i][j], y[i][j]) )
	else:
	  points.append( (x[i][j],y[i][j]) )
  return points

class NetCdfPreprocessorError(Exception):
  def __init__(self,value):
    self.value = value
  def __str__(self):
    return repr(self.value)
