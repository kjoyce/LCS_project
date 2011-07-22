import Scientific.IO.NetCDF as nc

class Generic_importer:
  def __init__(self,infilename):
# when implementing GUI this will throw an IOError exception if the NetCDF file is invalid.
    self.infile = nc.NetCDFFile(infilename,'r')

# to be implemented later, this
  def guess_variable_names(self):
    pass

      
class Ncom_importer(Generic_importer):
  pass
class Nat_importer(Generic_importer):
  pass
class Hfr_importer(Generic_importer):
