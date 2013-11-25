#!/usr/bin/python

import socket
from pymongo import Connection
import ConfigParser
#import os

class Info(object):
  ## Catch MongoDB data
  def __init__(self):
    self.get_config()

  def get_config(self):
    ## Catch config from config file
    config = ConfigParser.RawConfigParser()
    config.read('../conf/rpmController.ini')
    self.ip_mongo = config.get('mongo', 'ip')
    self.port_mongo = config.getint('mongo','port')
    self.db_mongo = config.get('mongo', 'database')

  def mongo_con(self, ip, port, rpmdb):
    connection = Connection(ip, port)
    return connection[rpmdb]

  def deleter(self, collection, rpm, status):
    ## Put deletef field of collection to true or false
    db = self.mongo_con(self.ip_mongo, self.port_mongo, self.db_mongo)
    code = db[collection].update({"name":rpm["name"], "version":rpm["version"], "release":rpm["release"]}, {'$set': {"deleted": status}})
    return code

  def collection_maker(self, collection, info_host, packages):
    ## Make a new collection if not exists
    db = self.mongo_con(self.ip_mongo, self.port_mongo, self.db_mongo)
    db[collection].insert(info_host)
    db[collection].insert(packages)
    
  def finder(self, collection, key, pattern):
    ## finder api 
    info_host = {}
    packages = []
    db = self.mongo_con(self.ip_mongo, self.port_mongo, self.db_mongo)
    db[collection].find({key:{'$regex':pattern}})

  def get_packages(self, collection):
    ## Catch all packages of MongoDB collection
    packages = []
    db = self.mongo_con(self.ip_mongo, self.port_mongo, self.db_mongo)
    for item in db[collection].find({"deleted":{'$exists': True}}):
      packages.append(item) 
    db[collection].disconnect
    return packages
