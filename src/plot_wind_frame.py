from velocityFrame import VelocityFrame 
import numpy as np

class WindVelocityFrame(VelocityFrame):
  """ This class is for plotting and analyzing wind velocity data from the
  NAM/WRF Mesoscale Forecast model.  It takes .nc files converted from their
  GRIB standard.  """
  def __init__(self,filename,mode):
    super(WindVelocityFrame,self).__init__(filename,mode)  

  def get_velocities_by_index(self,i,j):
    """ This returns the velocity vectors and their coordinates by given
    time(record number) and elevation index(pressure level)""" 
    u = self__ncfile.variables()['u']
    u = u[i][j]
    v = self__ncfile.variables()['v']
    v = v[i][j]
    x = self__ncfile.variables()['x']
    y = self__ncfile.variables()['y']
    x,y = np.meshgrid(x,y)
    return x,y,u,v

  def __set_map(self):
    lat_min = self.variables()['La1'][0]
    lon_min = self.variables()['Lo1'][0]
    
