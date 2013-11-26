#!/usr/bin/python

import socket
import ConfigParser
import logging
import sys
from pymongo import Connection



class Info(object):
  ## Catch MongoDB data
  def __init__(self):
    self.get_config()

  def get_config(self):
    ## Catch config from config file
    config = ConfigParser.RawConfigParser()
    try:
      logging.debug('Reading configuration')
      config.read('../conf/rpmController.ini')
    except:
      logging.critital('Error reading config file')

    self.ip_mongo = config.get('mongo', 'ip')
    self.port_mongo = config.getint('mongo','port')
    self.db_mongo = config.get('mongo', 'database')

  def mongo_con(self, ip, port, rpmdb):
    try:
      logging.debug('Trying to connect to: %s:%d', ip, port)
      connection = Connection(ip, port)
    except:
      logging.critical('Error Connecting to DB: %s:%d', ip, port)
      sys.exit(1)

    return connection[rpmdb]

  def mongo_con_(self):
    connection = Connection(self.ip_mongo, self.port_mongo)
    return connection[self.db_mongo]

  def deleter(self, collection, rpm, status):
    ## Put deletef field of collection to true or false
    db = self.mongo_con(self.ip_mongo, self.port_mongo, self.db_mongo)
    try:
      logging.debug('modifying RPM in MongoDB: %s', rpm["name"])
      code = db[collection].update({"name":rpm["name"], "version":rpm["version"], "release":rpm["release"]}, {'$set': {"deleted": status}})
    except:
      logging.critical('Error updating %s', rpm["name"])
    return code

  def collection_maker(self, collection, info_host, packages):
    ## Make a new collection if not exists
    db = self.mongo_con(self.ip_mongo, self.port_mongo, self.db_mongo)
    try:
      logging.debug('Making new collection')
      db[collection].insert(info_host)
      db[collection].insert(packages)
    except:
      logging.error('Error Making new collection %s', collection)
    
  def get_packages(self, collection):
    ## Catch all packages of MongoDB collection
    packages = []
    db = self.mongo_con(self.ip_mongo, self.port_mongo, self.db_mongo)
    try:
      logging.debug('Getting packages of %s', collection)
      for item in db[collection].find({"deleted":{'$exists': True}}):
        packages.append(item) 
      db[collection].disconnect

    except:
      logging.error('Error getting packages')
      raise

    return packages

  def print_collection(self, db_collection):
    for collection_ in db_collection.collection_names():
      if collection_ != "system.indexes":
        print collection_

  def print_info_host(self, fqdn):
    db = self.mongo_con(self.ip_mongo, self.port_mongo, self.db_mongo)
    rpms=db[fqdn]
    for host in rpms.find({"fqdn": "localhost.localdomain"}):
      print "id=%(_id)s fqdn=%(fqdn)s system=%(system)s release=%(SO_release)s version=%(SO_version)s date=%(date)s distribution=%(SO_distribution)s" % host
    for record in rpms.find({"deleted":{'$exists': True}}):
      # because record is a dict, we get you use lots of python magic
      # print "id=%(_id)s date=%(date)s version=%(version)s review_date=%(review_date)s name=%(name)s deleted=%(deleted)s release=%(release)s" % record  
      print "name=%(name)s-%(version)s-%(release)s date=%(date)s review_date=%(review_date)s deleted=%(deleted)s" % record  

  def print_info_rpms(self, fqdn, ip):
    db = self.mongo_con(self.ip_mongo, self.port_mongo, self.db_mongo)
    rpms=db[fqdn]
    for host in rpms.find({"ip": ip, "SO_release":{'$exists': True}}):
      print "id=%(_id)s fqdn=%(fqdn)s system=%(system)s release=%(SO_release)s version=%(SO_version)s date=%(date)s distribution=%(SO_distribution)s" % host
    for record in rpms.find({"ip": ip, "deleted":{'$exists': True}}):
      # because record is a dict, we get you use lots of python magic
      #print "id=%(_id)s date=%(date)s version=%(version)s review_date=%(review_date)s name=%(name)s deleted=%(deleted)s release=%(release)s" % record
      print "name=%(name)s-%(version)s-%(release)s date=%(date)s review_date=%(review_date)s deleted=%(deleted)s" % record  
