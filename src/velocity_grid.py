import os
import sys
import re
import numpy as np 
import Scientific.IO.NetCDF as nc
import  matplotlib.pyplot as plt
from scipy.interpolate import griddata
from mpl_toolkits.basemap import Basemap
from datetime import datetime,timedelta,tzinfo
from IPython.Debugger import Tracer; debug_here = Tracer()

#########################################################################
# Class: VelocityData
#
# The VelocityData class provides functions for datat that represents a time
# dependent vector field.  That is a collection of 2D velocity data grids
# indexed by a fixed time inteval.
#########################################################################
class VelocityData():
  def __init__(self,u,v,x,y,t,is_projected=False):
    for e in [u[0],v[0],x,y]:
      if(e.shape != x.shape):
	raise NetCdfPreprocessorError("Shape mismatch")

    for e in [u,v]:
      if( e.shape[0] != len(t) ):
	raise NetCdfPreprocessorError("Shape mismatch")
    self.is_projected = is_projected
    self.u = u
    self.v = v
    self.x = x
    self.y = y
    self.t = t
    self.__set_frames()

  def __set_frames(self):
    self.frames = []
    for i in range(len(self.t)):
      self.frames.append( VelocityFrame(self.u[i],self.v[i],self.x,self.y,self.t[i]))

  def stereo_proj(self,use_basemap=False):
    if self.is_projected:
      raise ProjectionError("This grid has already been projected")
    if use_basemap:
      pass
    else:
      u = self.u.copy()
      v = self.v.copy()
      x = self.x.copy()
      y = self.y.copy()
      for i in range(len(self.t)):
	frm = self.frames[i].stereo_proj(use_basemap)
	u[i] = frm.u
	v[i] = frm.v
	x = frm.x
	y = frm.y
      return VelocityData(u,v,x,y,self.t,is_projected='True')

  def get_recreate_parameters(self):
    return (self.u,self.v,self.x,self.y,self.t,self.is_projected)

  def export_txt(self,dirname):
    try:
      os.mkdir(dirname)
    except OSError as ex:
      if ex.errno == 17:  # ignore if the directory already exists.
	pass    
      else:
	raise ex

    for frm in self.frames:
      frm.export_txt( dirname+"/" )

  @staticmethod
  def import_txt(dirname):
    try:
      files = os.listdir(dirname)
    except OSError:
      raise ImportError("Couldn't open: "+dirname)
    frms = []
    time = []
    for f in files:
      try:
	frms.append(VelocityFrame.import_txt( dirname+"/"+ f))
	time.append( frms[-1].t )
      except ImportError:
	pass		  # ignore files in dir that dont match
      
    t = np.array(time)
    u = np.ones(( len(t), frms[0].u.shape[0], frms[0].u.shape[1] ))
    v = u.copy()
    for i in range(len(t)):
      u[i] = frms[i].u
      v[i] = frms[i].v

    return VelocityData(u,v,frms[0].x,frms[0].y,t)



#########################################################################
# Class: Velocity Frame
#
# This class provides functions for a velocity field at a fixed time.  
#########################################################################
class VelocityFrame():
  def __init__(self,u,v,x,y,t,is_projected=False):
    for e in [u,v,x,y]:
      if(e.shape != x.shape):
	raise NetCdfPreprocessorError("Shape mismatch")
    self.is_projected = is_projected
    self.u = u
    self.v = v
    self.x = x
    self.y = y
    self.t = t

  def quiver_plot(self):
    plt.figure()
    qplt =  plt.quiver(self.x,self.y,self.u,self.v)
    plt.hold(True)
    plt.show()
    return qplt
  
  def stereo_proj(self,use_basemap=False):
    if self.is_projected:
      raise ProjectionError("This grid has already been projected")
    if use_basemap:
      pass
    else:
      x,y = stereo_proj(self.x,self.y)
      xmin = x[-1][0]
      xmax = -x[-1][0]

      # find the height of the point directly below x[-1][0]
      ind = np.nonzero( x[0] > xmin )[0][0]
      ymin = y[0][ind]
      
      # find the height of midpoint of top row
      ymax = y[-1][ int(y.shape[1]/2) ]
      xx,yy = np.mgrid[xmin:xmax:x.shape[0]*1j,ymin:ymax:y.shape[1]*1j]
      uu = griddata((x.flatten(1),y.flatten(1)),self.u.flatten(1),(xx,yy),method='linear')
      vv = griddata((x.flatten(1),y.flatten(1)),self.v.flatten(1),(xx,yy),method='linear')
      return VelocityFrame(uu,vv,xx,yy,self.t,is_projected=True)

  def export_txt(self,dirname):
    try:
      os.mkdir(dirname)
    except OSError:
      pass

    for ti in range(len(self.t)):
      outfilename = self.dirname + "/" + self.t[ti].strftime("%Y%m%d%H%M") + ".txt"
      outfile = open(outfilename,'w')
      for i in range(self.lon.shape[0]):
	for j in range(self.lon.shape[1]):
	  outfile.write( "%f,%f,%f,%f\n" % (self.x[i][j],self.y[i][j],self.u[ti][i][j],self.v[ti][i][j]))
      outfile.close()
  
  def get_recreate_parameters(self):
    return (self.u,self.v,self.x,self.y,self.t,self.is_projected)

  def export_txt(self,prefix=''):
    outfilename = prefix + self.t.strftime("%Y%m%d%H%M") + ".txt"
    outfile = open(outfilename,'w')
    for i in range(self.x.shape[0]):
      for j in range(self.x.shape[1]):
	outfile.write( "%f,%f,%f,%f\n" % (self.x[i][j],self.y[i][j],self.u[i][j],self.v[i][j]))
    outfile.close()

  @staticmethod
  def import_txt(filename):
    to_match = ".*(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})\.txt$"
# We assume that each filename is named with a timestamp that is of the
# form <some_prefix><year><month><day><hour><min>.txt 
    m = re.match(to_match,filename)
    if not m:
      raise ImportError("Filename must end with timestamp")

    t = datetime(*[int(s) for s in m.groups()])
    fh = open(filename)
    d = dict()
    for l in fh:
      [alon,alat,au,av] = l.split(',')
      [alon,alat,au,av] = map(np.float64,[alon,alat,au,av])
      if alon in d.keys():
	d[alon].append( (alat,au,av) )
      else:
	d[alon] = [ (alat,au,av) ]

    N = len( d.keys() )
    M = len( d[d.keys()[0]])
    u = np.zeros( (len(d.keys()), len(d[d.keys()[0]])) )
    v = u.copy()
    x = u.copy()
    y = u.copy()
    for i in range(N):
      for j in range(M):
	x[i][j] = d.keys()[i]
	y[i][j] = d[d.keys()[i]][j][0]
	u[i][j] = d[d.keys()[i]][j][1]
	v[i][j] = d[d.keys()[i]][j][2]
    return VelocityFrame(u,v,x,y,t)

class ProjectionError(Exception):
  def __init__(self,value):
    self.value = value
  def __str__(self):
    return repr(self.value)
class ImportError(Exception):
  def __init__(self,value):
    self.value = value
  def __str__(self):
    return repr(self.value)


##########################################################################
# General Module functions
    
def stereo_proj(lon,lat):
  lon = lon.copy()
  lat = lat.copy()
  from numpy import meshgrid,pi,sin,cos,tan,abs
  R = 6378.1e3
  if(len(lon.shape) == 1):
    lon,lat = meshgrid(lon,lat)

# To minimize distortion, project from the pole in the opposite hemisphere.
  pole = 'north'
  if( lat[ int(lat.shape[0]/2) ][ int(lat.shape[1]/2) ] > 0 ):
    pole = 'south'
    lat = lat[ ::-1,:]  # reverse the order of rows

# Rotate to spherical coordinates.  I.e. assuming the longitude coordinates
# are sorted, make it the 0th meridian (which is irrelevant to
# stereographic projection) and measure latitude from the north pole.
  lon = lon - lon[0][0]
  lat = 90 - lat
  
  lat = pi/180*lat
  lon = pi/180*lon
  x = cos( lon ) / tan( lat/2 )
  y = sin( lon ) / tan( lat/2 )
# rotate so that the north pole is upwards
  x,y = rotate_pts(x,y,-(abs(lon[0][0]-lon[-1][-1])/2 + pi/2))
  if pole == 'south':
    lat = lat[ ::-1,:]

  return R*x,R*y

def rotate_pts(x,y,th):
  from numpy import sin,cos
  return (x*cos(th) - y*sin(th), x*sin(th) + y*cos(th))

