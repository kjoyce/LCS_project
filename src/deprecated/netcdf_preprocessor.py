import Scientific.IO.NetCDF as nc
import numpy as np
import datetime as dt

class NetCDF_Preprocessor:
  def __init__(self,filename,u_name,v_name,t_name,lon_name,lat_name,t0=dt.datetime(2000,1,1,0,0,0)):
    self.infile = nc.NetCDFFile(filename,'r')
    self.dirname = infilename[0:-3]
  
  def set_subgrid(self,lon_min,lon_max,lat_min,lat_max):
      

  def stgr_project(self,lon,lat):
    pass

  def export_txt(self):
    pass

