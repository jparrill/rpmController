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
import ConfigParser
import socket


# Para leer donde esta instalado el mongodb
config = ConfigParser.RawConfigParser()
config.read('/opt/pdi/rpmControler/rpmControler.ini')

ip_mongo = '127.0.0.1'
port_mongo = 27017


def find_collection():
  connection = Connection(ip_mongo, port_mongo)

  db = connection.rpmdb

  
  for collection_ in db.collection_names():
    if collection_ != "system.indexes":
      print collection_


def find_fqdn(fqdn):

  print "fqdn:",fqdn
  #fqdn = socket.getfqdn()

  #mongo = mongo_api.Info()
  #db = mongo_api.mongo_con(mongo.ip_mongo, mongo.port_mongo, fqdn)
  #db[collection].find({key:{'$regex':pattern}})
  #connect to mongodb
  
  connection = Connection(ip_mongo, port_mongo)

  # get database

  db = connection.rpmdb

  #get one collection

  
  #fqdn = socket.getfqdn()
  #fqdn = fqdn.replace("-", "_")
  #fqdn = fqdn.replace(".", "_")

  rpms = db[fqdn]
 
  for host in rpms.find({"fqdn": fqdn}):
    print "id=%(_id)s fqdn=%(fqdn)s system=%(system)s release=%(SO_release)s version=%(SO_version)s date=%(date)s distribution=%(SO_distribution)s" % host
  for record in rpms.find({"deleted":{'$exists': True}}):
    # because record is a dict, we get you use lots of python magic
    print "id=%(_id)s date=%(date)s version=%(version)s review_date=%(review_date)s name=%(name)s deleted=%(deleted)s release=%(release)s" % record
  

def find_ip(ip):
  print "ip:",ip
  connection = Connection(ip_mongo, port_mongo)

  # get database

  db = connection.rpmdb

  #get one collection

  for test in db.collection_names():
    print test

  
    rpms = db[test]
 
    for host in rpms.find({"ip": ip, "SO_release":{'$exists': True}}):
      print "id=%(_id)s fqdn=%(fqdn)s system=%(system)s release=%(SO_release)s version=%(SO_version)s date=%(date)s distribution=%(SO_distribution)s" % host
    for record in rpms.find({"ip": ip, "deleted":{'$exists': True}}):
      # because record is a dict, we get you use lots of python magic
      print "id=%(_id)s date=%(date)s version=%(version)s review_date=%(review_date)s name=%(name)s deleted=%(deleted)s release=%(release)s" % record



def main():

  try:
    optsList, argsList = getopt.getopt(sys.argv[1:], "l:i:h:")

  except getopt.GetoptError, err:
    #Error handling for unknown or incorrect number of options
    print str(err)
    sys.exit(2)

  #dependiendo del parametro hago un find u otro


  for opt, arg in optsList:
    if opt in ('-l', '--list'):
        find_collection()
    elif opt in ('-h', '--host'):
        find_fqdn(arg)
    elif opt in ('-i', '--ip'):
        find_ip(arg)
    else:
        print "Unhandled option"
        sys.exit(2)
  


main()
