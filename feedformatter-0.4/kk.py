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
from feedformatter  import Feed
import time



def run():


  # Create the feed
  feed = Feed()

  # Set the feed/channel level properties
  feed.feed["title"] = "RPMS Installados"
  feed.feed["link"] = "http://pspaco2"
  feed.feed["author"] = "troitino"
  feed.feed["description"] = "Avisa cuando un rpm es instalado en una maquina"



  #connect to mongodb

  connection = Connection('pspaco.hi.inet', 27017)

  # get database

  db = connection.rpms_database

  #get one collection

  collection = db.rpms_collection


  info_pcs = db.info_hosts


  rpms = db.rpms

  id_=""

  for host in info_pcs.find():
      id_=host["id_"]
      for record in rpms.find({"id_": id_}):
         print "id=%(_id)s id_=%(id_)s name=%(rpm)s date_process=%(date_process)s date_installed=%(date_installed)s" % record

         
         cadena = str(record["rpm"]) + str(record["date_process"]) + str(record["date_installed"])

         # Create an item
         item = {}
         item["title"] = str(host["name"])
         #item["link"] = "http://www.example.com/example_url"
         item["description"] = cadena
         item["pubDate"] = time.localtime()
         item["guid"] = str(record["_id"])
         print time.localtime()
         feed.items.append(item)

# Print the feed to stdout in various formats
#print feed.format_rss1_string()
#print feed.format_rss2_string()
#print feed.format_atom_string()

# Save the feed to a file in various formats
#  feed.format_rss1_file("example_feed_rss1.xml")
  feed.format_rss2_file("example_feed_rss2.xml")
#  feed.format_atom_file("example_feed_atom.xml")


def main():

    run()

main()
