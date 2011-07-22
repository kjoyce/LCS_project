from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from Scientific.IO.NetCDF import NetCDFFile
from IPython.Debugger import Tracer; debug_here = Tracer()

class VelocityFrame(object):
  """ This class extends the Scientific.IO.NetCDFFile library and uses the
  basemap libraries for plotting NetCDF files from NOAA"""
  def __init__(self,filename,mode):
    self.__ncfile = NetCDFFile(filename,mode)
  
  def masked_array(self,varname,maskval):
    var = self.__ncfile.variables[varname][:]
    m = (var == maskval)
    return np.ma.masked_array(var,mask=m)

  def variables(self):
    return self.__ncfile.variables

  def nc_attributes(self):
    return self.__ncfile.__dict__

