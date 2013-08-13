#!/usr/bin/python

import platform
import datetime
import time
import os
from pymongo import Connection
import datetime
import time
import hashlib
import codecs
import sys
import getopt


def run(string, busqueda):

  #connect to mongodb
  
  connection = Connection('pspaco.hi.inet', 27017)

  # get database

  db = connection.rpms_database

  #get one collection

  collection = db.rpms_collection


  info_pcs = db.info_hosts


  rpms = db.rpms
 
  id_=""

  if busqueda == "IP":
    #print "option: IP"
    for host in info_pcs.find({"ips": string}):
      print "id=%(_id)s id_=%(id_)s name=%(name)s ips=%(ips)s date=%(date)s system=%(system)s release=%(release)s version=%(version)s distribution=%(distribution)s" % host
      id_=host["id_"]
    for record in rpms.find({"id_": id_}):
      # because record is a dict, we get you use lots of python magic
      print "id=%(_id)s id_=%(id_)s name=%(rpm)s date_process=%(date_process)s date_installed=%(date_installed)s" % record
  elif busqueda == "HOST":
    #print "option: HOST"
    for host in info_pcs.find({"name": string}):
      print "id=%(_id)s id_=%(id_)s name=%(name)s ips=%(ips)s date=%(date)s system=%(system)s release=%(release)s version=%(version)s distribution=%(distribution)s" % host
      id_=host["id_"]
    for record in rpms.find({"id_": id_}):
      # because record is a dict, we get you use lots of python magic
      print "id=%(_id)s id_=%(id_)s name=%(rpm)s date_process=%(date_process)s date_installed=%(date_installed)s" % record
  elif busqueda == "ONLYHOST":
    for host in info_pcs.find({"name": string}):
      print "id=%(_id)s id_=%(id_)s name=%(name)s ips=%(ips)s date=%(date)s system=%(system)s release=%(release)s version=%(version)s distribution=%(distribution)s" % host
      id_=host["id_"]
  elif busqueda == "ONLYRPM":
    #print "option: ONLYRPM"
    for host in info_pcs.find({"name": string}):
      #print "id=%(_id)s id_=%(id_)s name=%(name)s ips=%(ips)s date=%(date)s system=%(system)s release=%(release)s version=%(version)s distribution=%(distribution)s" % host
      id_=host["id_"]
    for record in rpms.find({"id_": id_}):
      # because record is a dict, we get you use lots of python magic
      print "id=%(_id)s id_=%(id_)s name=%(rpm)s date_process=%(date_process)s date_installed=%(date_installed)s" % record
  

             

def main():

  try:
    optsList, argsList = getopt.getopt(sys.argv[1:], "i:h:o:r:", ["ip=", "host=", "onlyhost", "onlyrpm"])

  except getopt.GetoptError, err:
    #Error handling for unknown or incorrect number of options
    print str(err)
    sys.exit(2)

  #dependiendo del parametro hago un find u otro

  for opt, arg in optsList:
    if opt in ('-i', '--ip'):
        ip_find = arg
        run(arg,"IP")
    elif opt in ('-h', '--host'):
        run(arg,"HOST")
    elif opt in ('-o', '--onlyhost'):
        run(arg,"ONLYHOST")
    elif opt in ('-r', '--onlyrpm'):
        run(arg,"ONLYRPM")
    else:
        print "Unhandled option"
        sys.exit(2)   

main()