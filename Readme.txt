This is the base directory for the LCS project. The 'src/' directory contains
all of the python source code for the LCS computation and data preprocessing.
The directories 'ocean_data' and 'wind_data' contain various data sources and
soft-links to the python source code for convenience.   The 'libs' directory
contains all of the required libraries other than Python 2.7.1+

The Panopoly directory contains the Java program for viewing Netcdf data.  This
is especially useful for getting a quick idea of the data and metadata of new
netcdf files.

The file usage_example.py gives an example of implementing the data
preprocessing NCOM ocean current data and NAM wind model data.
