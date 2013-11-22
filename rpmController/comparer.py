import rpm_api
import mongo_api
import pprint

def formatter(collection):
    collection = collection.replace("-", "_")
    collection = collection.replace(".", "_")
    return collection

def analize(rpm, mongo_packages):
  pkg_list = []
  last = '0'
  if mongo_packages != []:  
    for mongo_rpm in mongo_packages:
      if mongo_rpm["deleted"] == 'true':
        ## If element is a deleted RPM will not valuate
        pass

      else:
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

def merger(rpm_packages, mongo_packages):
  unique_list = []
  for rpm in rpm_packages:
    pkg_status = analize(rpm, mongo_packages)
    if pkg_status == '0':
      ## Rpm Exists in MongoDB
      pass

    if pkg_status == '1':
      ## The rpm is not exist, append!!
      unique_list.append(rpm)

    if pkg_status == '2':
      ## If the Collection is empty
      print "Collection Empty, fullfilling..."
      unique_list.extend(rpm_packages)
      break

  return unique_list




info_host = {}
packages = []
rpms = rpm_api.Info()
info_host, packages = rpms.catcher()

mongo = mongo_api.Info()
mongo_packages = mongo.get_packages(formatter(info_host['fqdn']))
merged_packages = merger(packages,mongo_packages)

if merged_packages == []:
  print "there is not changes in the Node"
else:
  mongo.collection_maker(formatter(info_host['fqdn']), info_host, merged_packages)


#print merged_list
## Show info
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(merged_packages)



