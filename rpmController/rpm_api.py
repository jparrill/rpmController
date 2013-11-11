import platform
import socket
import time
import rpm
import pprint

class Info(object):
  def __init__(self):
    pass

  def rpm_getinfo(self):
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
    
  def catcher(self):
    packages = []
    info_host = {}
    info_host['fqdn'] = socket.getfqdn()
    info_host['ip'] = socket.gethostbyname(socket.gethostname())
    info_host['date'] = time.ctime(time.time())
    info_host['system'] = platform.system()
    info_host['release'] = platform.release()
    info_host['version'] = platform.version()
    info_host['distribution'] = platform.dist()
    packages = self.rpm_getinfo()
    ## Show info
    #print info_host
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(packages)
    ##
    return info_host, packages

