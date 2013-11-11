import rpm_api
import mongo_api
import pprint
import unicodedata

def formatter(collection):
    collection = collection.replace("-", "_")
    collection = collection.replace(".", "_")
    return collection

info_host = {}
packages = []
rpms = rpm_api.Info()
info_host, packages = rpms.catcher()

#mongo_api.Info(formatter(info_host['fqdn']),info_host, packages)
mongo = mongo_api.Info()
mongo_packages = mongo.get_packages(formatter(info_host['fqdn']))

mergedlist = set(packages + mongo_packages)

## Show info
#print info_host
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(mongo_packages)

print type(mergedlist)


