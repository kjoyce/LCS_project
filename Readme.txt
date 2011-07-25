Readme.txt last updated 25 Jul 2011 by Kevin Joyce

This is the base directory for the LCS project. The 'src/' directory contains
all of the python source code for the LCS computation and data preprocessing.
The directories 'ocean_data' and 'wind_data' contain various data sources and
soft-links to the python source code for convenience.   The 'libs' directory
contains all of the required libraries other than Python 2.7.1+

The Python and Matlab source code has a github repository.  The project is 
currently under the username kjoyce.  You can checkout the most recent version
by running `git checkout`.  

The Panopoly directory contains the Java program for viewing Netcdf data.  This
is especially useful for getting a quick idea of the data and metadata of new
netcdf files.

The libs/ directory contains the source code to all of the non-standard Python
libraries that have been used throughout development.  Many of these are not 
used anymore, but could become useful.  I.e. pygrib-1.8.3 can be used to read
GRIB type data, but is not implemented.  Similairly, the netcdf-4.1.1 provides
 different, and perhaps faster, libraries for reading NetCDF data files.

The mangen144/ directory has the source code for the  C++ implementation by
Shawn Shadden.  This could be useful as a reference.  

The ocean_data/ directory contains ocean current velocity data from the HFRNET
satelite ocean current data, and NCOM ocean current model data.

The src/ directory contains all of the Python and Matlab source code.  The folder
src/deprecated has old and test functions that are no longer up to date but
may be useful for reference.

The trash/ directory is for test output files or test code that may be useful
for reference later, but is otherwise not applicable.

The useful_docs/ directory contains documentation for data sources and algorithms
used on the project.

The wind_data/ directory contains wind velocity data from the Nat database.  

