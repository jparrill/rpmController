import rpm_api
import mongo_api
import pprint
import unicodedata

def formatter(collection):
    collection = collection.replace("-", "_")
    collection = collection.replace(".", "_")
    return collection

def merger(rpm_packages, mongo_packages):
	unique_list = []
	for i in rpm_packages:
		if i not in mongo_packages:
			unique_list.append(i)
	return unique_list

info_host = {}
packages = []
rpms = rpm_api.Info()
info_host, packages = rpms.catcher()

mongo = mongo_api.Info()
mongo_packages = mongo.get_packages(formatter(info_host['fqdn']))

merged_packages = merger(packages, mongo_packages)

#print merged_list
## Show info
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(merged_packages)



