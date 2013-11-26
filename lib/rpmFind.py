#!/usr/bin/python


from pymongo import Connection
import sys
import getopt
import ConfigParser

from os import path
sys.path.append("../lib")
from rpmController import mongo_api

# Para leer donde esta instalado el mongodb
config = ConfigParser.RawConfigParser()
config.read('/opt/pdi/rpmControler/rpmControler.ini')

ip_mongo = '127.0.0.1'
port_mongo = 27017


def find_collection():


  mongo = mongo_api.Info()
  db = mongo.mongo_con_()

  mongo.print_collection(db)


def find_fqdn(fqdn):
  mongo = mongo_api.Info()
  mongo.print_info_host(fqdn)



def find_ip(ip):
  mongo = mongo_api.Info()
  db = mongo.mongo_con_()
 
  for test in db.collection_names():
    mongo.print_info_rpms(test,ip)


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
