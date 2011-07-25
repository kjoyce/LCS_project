import os
import sys
import re
import numpy as np 
import Scientific.IO.NetCDF as nc
from datetime import datetime,timedelta,tzinfo
import velocity_grid as vg
reload(vg)
VelocityData = vg.VelocityData
VelocityFrame = vg.VelocityFrame
#from velocity_grid import VelocityData,VelocityFrame
#from IPython.Debugger import Tracer; debug_here = Tracer()

class Generic_importer:
  def __init__(self,infilename):
# when implementing GUI this will throw an IOError exception if the NetCDF file is invalid.
    self.infile = nc.NetCDFFile(infilename,'r')

  def get_vel_data(self):
    self._load_t_data()
    self._load_coordinate_data()
    self._load_vector_data()
    return VelocityData(self.u,self.v,self.x,self.y,self.t)

# Each of these does fairly generic behavior.  For capturing a subset of the
# data, or unit conversions, or other preprocessing overload these functions.
# See Ncom_importer
  def _load_t_data(self):
    self.t = self.infile.variables[self.time_var]
  def _load_coordinate_data(self):
    x = self.infile.variables[self.lon_var]
    y = self.infile.variables[self.lat_var]
    self.x,self.y = np.meshgrid(x,y)
  def _load_vector(self):
    self.u = self.infile.variables[self.u_var]
    self.v = self.infile.variables[self.v_var]

  def guess_variables(self):
    # This is yet to be implemented but it tries to guess the variables
    raise NetCdfPreprocessorError("Tried guessing variable names but failed.")

#########################################################################
# Class: Ncom_importer
# Inherit: Generic_importer
#
# This class provides functions for importing data from NCOM NetCDF 
# output.  It also provides functions for cropping
# to the Alaska Gulf region.
#########################################################################
class Ncom_importer(Generic_importer):
  def __init__(self,infilename,region=None):
    self.min_lon,self.max_lon,self.min_lat,self.max_lat = self.get_region(region)

# not yet implemented
#    if os.path.isdir(infilename):
#      self.import_txt(infilename)
#      self.dirname = infilename
#    else:
    self.infile = nc.NetCDFFile(infilename,'r')
    self.infilename = infilename
    self.dirname = infilename[0:-3]
    self.time_var = 'time'
    self.lon_var = 'lon'
    self.lat_var = 'lat'
    self.u_var = 'water_u'
    self.v_var = 'water_v'

    Generic_importer.__init__(self,infilename)

  def get_region(self,region):
    if region == "AK_gulf":
      return -170,-120,45,70 # coordinates for gulf of Alaska.
    else:
      return -180,180,-90,90 # the whole globe

  def _load_coordinate_data(self):
    X = self.infile.variables['lon'].getValue()
    Y = self.infile.variables['lat'].getValue()
    deltay = abs(Y[-1] - Y[0]) / Y.shape[0]
    deltax = abs(X[-1] - X[0]) / X.shape[0] 
    
    # This finds the indicies that coorespond with desired dimensions.
    x0 = int(abs(360+self.min_lon-X[0])/deltax)
    x1 = int(abs(360+self.max_lon-X[0])/deltax)

    # This finds the indicies that coorespond with desired dimensions.  These
    # particular files measure latitude using spherical coordinates i.e. 0
    # (South Pole) to 180 (North Pole).  The initial latitude is not zero due
    # to Antarctica.
    y0 = int(abs(self.min_lat - Y[0])/deltay)
    y1 = int(abs(self.max_lat - Y[0])/deltay)

    self.min_lon_idx = x0
    self.max_lon_idx = x1

    self.min_lat_idx = y0
    self.max_lat_idx = y1

    self.x,self.y = np.meshgrid( X[x0:x1], Y[y0:y1] )

  def _load_vector_data(self):
    try:
      x0 = self.min_lon_idx
      x1 = self.max_lon_idx
      y0 = self.min_lat_idx
      y1 = self.max_lat_idx
    except NameError:
      raise NetCdfPreprocessorError("Must load coordinate data first")

    Tlen = self.infile.variables['water_u'].shape[0]
    self.u = np.zeros( (Tlen,(y1-y0),(x1-x0)))
    self.v = np.zeros( (Tlen,(y1-y0),(x1-x0)))
    for t in range(Tlen):
      self.u[t] = self.infile.variables['water_u'][t][0][y0:y1][:,x0:x1]
      self.v[t] = self.infile.variables['water_v'][t][0][y0:y1][:,x0:x1]
  
  def _load_t_data(self):
    T = self.infile.variables['time'].getValue()
    self.t = [NcomTime(int(x)) for x in T]

class NcomTime(datetime):
  def __new__(cls,hrs):
    d = timedelta(hours=hrs)
    t0=datetime(2000,1,1,0,0,0)
    return d + t0

#########################################################################
# Class: Nat_importer
# Inherit: Generic_importer
#
# This class provides functions for importing data from NAT Gulf of Alaska
# wind velocity NetCDF output.  
#########################################################################
class Nat_importer(Generic_importer):
  def __init__(self,infilename):
    self.infile = nc.NetCDFFile(infilename,'r')
    self.time_var = 'valtime'
    self.lon_var = 'x'
    self.lat_var = 'y'
    self.u_var = 'u'
    self.v_var = 'v'
    self.levels = self.infile.variables['level'].getValue()
    self.lev_dict = dict([(self.levels[i], i) for i in range(len(self.levels))])

  def _load_t_data(self):
    T = self.infile.variables[self.time_var].getValue()
    self.t = [NamTime(int(x)) for x in T]
    
  def get_vel_data(self,level):
    if level not in self.levels:
      raise NetCdfPreprocessorError("Invalid altitude.  See attribute levels")

    self._load_t_data()
    self._load_coordinate_data()
    self._load_vector_data(level)
    return VelocityData(self.u,self.v,self.x,self.y,self.t,is_projected=True)
    
  def _load_vector_data(self,level):
    idx = self.lev_dict[level]
    self.u = np.ones( (len(self.t), self.x.shape[0], self.x.shape[1]) )
    self.v = np.ones( (len(self.t), self.x.shape[0], self.x.shape[1]) )
    for i in range(len(self.t)):
      self.u[i] = self.infile.variables['u'][i][idx]
      self.v[i] = self.infile.variables['v'][i][idx]

class NamTime(datetime):
  def __new__(cls,hrs):
    d = timedelta(hours=hrs)
    t0 = datetime(1992,1,1,0,0,0)
    return d + t0


#########################################################################
# Class: Hfr_importer
# Inherit: Generic_importer
#
# This class provides functions for importing data from HF Radar Satelite
# ocean current velocity NetCDF data
#########################################################################
class Hfr_importer(Generic_importer):
  pass 

class NetCdfPreprocessorError(Exception):
  def __init__(self,value):
    self.value = value
  def __str__(self):
    return repr(self.value)
