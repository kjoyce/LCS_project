from velocityFrame import VelocityFrame
from mpl_toolkits.basemap import Basemap
import numpy as np

class OceanVelocityFrame(VelocityFrame):
  """ This class extends the Scientific.IO.NetCDFFile library and uses the
  basemap libraries for plotting NetCDF files from NOAA"""
  def __init__(self,filename,mode):
    super(OceanVelocityFrame,self).__init__(filename,mode)  

  def velocities(self):
    mask = -32768
    u = self.masked_array('u',mask)
    v = self.masked_array('v',mask)
    x = self.variables()['lon'][:]
    y = self.variables()['lat'][:]
    return x,y,u[0],v[0]

  def barb_plot_frame(self):
    x,y,u,v = self.__set_map()
    self.__basemap.barbs(x,y,u,v)
    self.__basemap.drawcoastlines()

  def __set_map(self):
    attr = self.nc_attributes()
    lat_min = attr['geospatial_lat_min'][0]
    lat_max = attr['geospatial_lat_max'][0]
    lon_min = attr['geospatial_lon_min'][0]
    lon_max = attr['geospatial_lon_max'][0]

    self.__basemap = Basemap(projection='cyl',
			    llcrnrlat = lat_min,
			    urcrnrlat = lat_max,
			    llcrnrlon = lon_min,
			    urcrnrlon = lon_max,
			    resolution = 'l')

    x,y,u,v = self.velocities()
    x,y = np.meshgrid(x,y)
    return x,y,u,v

  def quiver_plot_frame(self):
    x,y,u,v = self.__set_map()
    self.__basemap.quiver(x,y,u,v)
    self.__basemap.drawcoastlines()

