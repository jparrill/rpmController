import platform
import socket
import time
import rpm
import logging

class Info(object):
  ## This class take the information of the rpms attacking to the RPM's api  and host information 
  def __init__(self):
    pass

  def rpm_getinfo(self):
    ## Catch all rpm installed in the system only for CentOS/RedHat/Fedora
    rpm_collect = []
    rpm_struct = {}
    try:
      logging.debug('Getting information of installed RPM')
      db = rpm.TransactionSet()
      rpm_packages = db.dbMatch()
    except:
      logging.critical('Error getting information about rpms installed')
      raise

    for package in rpm_packages:
      rpm_struct['name'] = package['name']
      rpm_struct['version'] = package['version']
      rpm_struct['release'] = package['release']
      rpm_struct['date'] = package.sprintf("%{INSTALLTID:date}")
      rpm_struct['review_date'] = time.ctime(time.time())
      rpm_struct['deleted'] = 'false'
      rpm_struct['ip'] = socket.gethostbyname(socket.gethostname())
      if rpm_struct not in rpm_collect:
        rpm_collect.append(rpm_struct.copy())

    return sorted(rpm_collect)
    
  def catcher(self):
    ## Catch information of the node
    packages = []
    info_host = {}
    info_host['fqdn'] = socket.getfqdn()
    info_host['ip'] = socket.gethostbyname(socket.gethostname())
    info_host['date'] = time.ctime(time.time())
    info_host['system'] = platform.system()
    info_host['SO_release'] = platform.release()
    info_host['SO_version'] = platform.version()
    info_host['SO_distribution'] = platform.dist()
    packages = self.rpm_getinfo()

    return info_host, packages

