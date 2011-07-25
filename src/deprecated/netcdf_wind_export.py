import Scientific.IO.NetCDF as nc
import sys
import os

from datetime import datetime,timedelta,tzinfo
class NamTime(datetime):
  def __new__(cls,hrs):
    d = timedelta(hours=hrs)
    t0 = datetime(1992,1,1,0,0,0)
    return d + t0

class NamNetcdf(NetCdfExporter):
if len(sys.argv) < 2: 
  print "\n Usage: python " + sys.argv[0] +" <NETCDF_FILE>.nc\n"
  sys.exit()

for infilename in sys.argv[1:]:
  try:
    infile = nc.NetCDFFile(infilename,'r')
  except IOError:
    print "Could not read: %s" % infilename
    continue

  X = infile.variables['x'].getValue()
  Y = infile.variables['y'].getValue()

  u = infile.variables['u'].getValue()
  v = infile.variables['v'].getValue()
  
  T = [NamTime(int(x)) for x in infile.variables['valtime'].getValue()]
  L = infile.variables['level'].getValue()

  dirname = infilename[0:-3]
  try:
    os.mkdir(dirname)
  except OSError:
    pass

# The default value for a NAN, see documentation
  NAN = -9999
  for l in range(len(L)):
    wdir = dirname + ("%dhPa" % L[l])
    try:
      os.mkdir(wdir)
    except OSError:
      pass
    for k in range(len(T)):
      outfilename = wdir + "/nam16_" + grid_name + "_" + T[k].strftime("%Y%m%d%H%M_") + ".txt"
      outfile = open(outfilename,'w')
      for i in range(len(X)):
	for j in range(len(Y)):
	  if u[k][l][j][i] > NAN or v[k][l][j][i] > NAN:
	    outfile.write( 
	      "%f,%f,%f,%f\n" % (X[i],Y[j],u[k][l][j][i],v[k][l][j][i]) 
	    )
      outfile.close()


