""" download_data.py 
This short script can be used for downloading data for the for HFRNet satelite
ocean current data, NCOM ocean current model data, or NAM wind velocity model
data
"""
import ftplib
import socket
import sys
import os
from datetime import date
from IPython.Debugger import Tracer; debug_here = Tracer()

OPT1 = ('HFRNet ocean data','NCOM ocean data','NAM wind data','help')
opt = prompt_arr_choice(OPT1)
DATA
if opt == OPT1[0]:
  HOST = 'sandbox.ucsd.edu'
  DIR  = 'pub/CORDC/outgoing/HFRNet'

  try:
    host = ftplib.FTP(HOST)
    host.login()
    host.cwd(DIR)
  except (socket.error, socket.gaierror, ftplib.error_perm), e:
    print 'Cannot reach host: ftp://%s/%s' % (HOST,DIR)

  print "Connected to: ftp://%s/%s" % (HOST,DIR)

  SITES = ('AKNS','GAK','PRVI','USEGC','USHI','USWC')
  RES = ('500m','1km','2km','6km')

  print "Select site to sync:"
  site = prompt_arr_choice(SITES)
  host.cwd(site)

  print "Select resolution:"
  res = prompt_arr_choice(RES)

  hostfiles = HFRNetHostFiles(res)
  host.dir(hostfiles.digest)

  curfiles = os.listdir(site)
  to_get = set(hostfiles.filenames) - set(os.listdir(site))

  print "The following files will be downloaded:"
  for f in to_get:
    print f
  dnld = raw_input("Do you wish to proceed (y/n)?")
  if dnld == 'y' or dnld == 'yes':
    for f in to_get:
      print "Downloading %s..." % f
      fl = open("%s/%s" % (site,f),'wb')
      host.retrbinary('RETR %s' % f,fl.write)
      fl.close()
elif opt == OPT1[1]:
  pass  
elif opt == OPT1[2]:
  pass
elif opt == OPT1[3]:
  pass

def prompt_arr_choice(arr):
  for i in range(len(arr)):
    print "(%d) %s" % (i,arr[i])
  try: 
    n = int(raw_input("choice:"))
    choice = arr[n]
  except ValueError:
    print "Invalid Choice"
    choice = prompt_arr_choice(arr)
  return choice


class HFRNetHostFiles:
  def __init__(self,res,date=0):
    self.filenames = []
    self.resolution = res
    self.date = date
  def digest(self,line):
    filename = line.split()[-1]
    try:
      ares = filename.split('_')[3]
    except:
      ares = ''
    if ares == res:
      self.filenames.append(line.split()[-1])
