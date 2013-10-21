#!/usr/bin/python

import platform
import socket
import time
import os
from pymongo import Connection
import datetime
import ConfigParser
import rpm
import pprint

## config file have the place of MongoDB
config = ConfigParser.RawConfigParser()
config.read('../conf/rpmController.ini')

ip_mongo = config.get('mongo', 'ip')
port_mongo = config.getint('mongo','port')
db_mongo = config.get('mongo', 'database')

def rpm_getinfo():
  rpm_collect = []
  rpm_struct = {}
  db = rpm.TransactionSet()
  rpm_packages = db.dbMatch()

  for package in rpm_packages:
    rpm_struct['name'] = package['name']
    rpm_struct['version'] = package['version']
    rpm_struct['release'] = package['release']
    rpm_struct['date'] = package.sprintf("%{INSTALLTID:date}")
    rpm_struct['review_date'] = time.ctime(time.time())
    rpm_struct['deleted'] = False
    if rpm_struct not in rpm_collect:
      rpm_collect.append(rpm_struct.copy())

  return sorted(rpm_collect)
  
def run():
  packages = []
  info_host = {}
  info_host['name'] = socket.getfqdn()
  info_host['ip'] = socket.gethostbyname(socket.gethostname())
  info_host['date'] = time.ctime(time.time())
  info_host['system'] = platform.system()
  info_host['release'] = platform.release()
  info_host['version'] = platform.version()
  info_host['distribution'] = platform.dist()
  packages = rpm_getinfo()
  ## Show info
  print info_host
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(packages)
  ##

def mongo_con(ip, port, rpmdb):
  connection = Connection(ip, port)
  db = connection.rpmdb
  return db.rpms_collection

run()
collection = mongo_con(ip_mongo, port_mongo, db_mongo)
