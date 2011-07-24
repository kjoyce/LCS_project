# Here is an example of pre processing NCOM ocean current veloctiy data
from netcdf_import import Ncom_importer

importer = Ncom_importer('ocean_data/NCOM/ncom_glb_sfcurrents_2011060900.nc')
vel_data = importer.get_vel_data()

vel_data.frames[0].quiver_plot()
vel_data.frames[0].stereo.quiever_plot()

# Here we advect each grid point from the intitial time frame to the 5th
# time frame
points = vel_data.advect( vel_data.t[0], vel_data.t[5] )

