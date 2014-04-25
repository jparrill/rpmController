import mongo_api
import time

class Comparer(object):
  def __init__(self):
    pass

  def formatter(self, collection):
    ## Change name of collection
      collection = collection.replace("-", "_")
      collection = collection.replace(".", "_")
      return collection

  def rpm_analize(self, rpm, mongo_packages):
    ## Comparison between 1 rpm and all rpm_packages storaged in MongoDB
    ## Purpose: Know if the rpm is in MongoDB
    pkg_list = []
    last = '0' 
    if mongo_packages != []:  
      for mongo_rpm in mongo_packages:
        if rpm['name'] == mongo_rpm["name"] and rpm['version'] == mongo_rpm["version"] and rpm['release'] == mongo_rpm["release"]:
          ## Rpm exist in Mongo_list
          status = '0'
          last = '1'
          break

        if last == '0':
          ## If there is not RPM in Mongo_list
          status = '1'

    else:
      # Empty collection
      status = '2'

    return status

  def mongo_analize(self, mongo_rpm, rpm_packages):
    ## Comparison between 1 rpm storaged in MongoDB and all rpm_packages of the node
    ## Purpose: Mark 1 rpm in MongoDB as Deleted
    for rpm in rpm_packages:
      if rpm['name'] == mongo_rpm["name"] and rpm['version'] == mongo_rpm["version"] and rpm['release'] == mongo_rpm["release"] and mongo_rpm["deleted"] == 'false':
        status = '0'
        break

      elif rpm['name'] == mongo_rpm["name"] and rpm['version'] == mongo_rpm["version"] and rpm['release'] == mongo_rpm["release"] and mongo_rpm["deleted"] == 'true':
        ## Update Mongo with this rpm as installed
        status = '3'
        break

      elif mongo_rpm["deleted"] == 'true':
        status = '0'

      else:
        status = '1'

    return status

  def merger(self, rpm_packages, mongo_packages, method, collection):
    ## Collection parameter is for Mongo method
    unique_list = []
    updates = 0
    if method == 'rpm':
      for rpm in rpm_packages:
        pkg_status = self.rpm_analize(rpm, mongo_packages)
        if pkg_status == '0':
          ## Rpm Exists in MongoDB
          pass

        elif pkg_status == '1':
          ## The rpm is not exist, append!!
          print "** Adding package on MongoDB: %s" % rpm['name'] 
          unique_list.append(rpm)
          updates += 1

        elif pkg_status == '2':
          ## If the Collection is empty
          print "Collection Empty, fullfilling..."
          unique_list.extend(rpm_packages)
          break

      return unique_list, updates

    elif method == 'mongo':
      updates = 0
      mongo = mongo_api.Info()
      for mongo_rpm in mongo_packages:
        pkg_status = self.mongo_analize(mongo_rpm, rpm_packages)
        if pkg_status == '0':
          ## Rpm Exists in MongoDB or is deleted
          pass

        elif pkg_status == '1':
          ## The rpm is not exist in the node, lets erase in MongoDB
          ## the last parameter is to set true or false the deleted fliend in MongoDB
          try:
            print "** Updating package on MongoDB: %s" % mongo_rpm['name'] 
            code = mongo.deleter(collection, mongo_rpm, 'true', time.ctime(time.time()))
            updates += 1 

          except:
            print "Error Updating MongoDB %s collection" % collection
            raise  

        elif pkg_status == '3':
          ## RPM was erased and reinstalled
          print "** Updating package on MongoDB: %s" % mongo_rpm['name']
          code = mongo.deleter(collection, mongo_rpm, 'false', time.ctime(time.time()))
          updates += 1

      return updates   



