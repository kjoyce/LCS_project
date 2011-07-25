# Here is an example of pre processing NCOM ocean current veloctiy data
from netcdf_import import Ncom_importer

importer = Ncom_importer('../ocean_data/NCOM/ncom_glb_sfcurrents_2011060900.nc','AK_gulf')
vel_data = importer.get_vel_data()
vel_data.frames[0].quiver_plot()

stereo_vel_data = vel_data.stereo_proj()
stereo_vel_data.frames[0].quiever_plot()

stereo_vel_data.export_txt('TEST_OUTPUT')

# Here is an example of preprocessing NAT16 wind current velocity data

importer = Nat_importer('../wind_data/NAM216/2011060900_nam216.nc')
