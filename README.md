RPM Controller
=========

RPM Controller is a utillity that take control of all RPM's installed, erased and updated in the machine, this information goes to a central MongoDB Node

Version
----

0.1

Tech
-----------

RPM Controller use this technologies:

* [python] - Awesome developing languaje, supported from 2.6
* [rpm_api] - Own Library that take information about rpm's of the node
* [pymongo] - Great module that talks with MongoDB
* [argparse] - Argument parser Module

Installation
--------------
How to install module:
```sh
git clone git@pdihub.hi.inet:troitino/rpmControler.git
```
or:
```sh
yum install rpmController
```

##### Configure file:

* conf/rpmController.ini

```sh
[mongo]
 ip = 127.0.0.1    --> IP of MongoDB Node
 port = 27017      --> Port of MongoDB Node
 database = rpmdb  --> Database Name
```

Execution
--------------
By default RPM Controller search RPMs in the system and registry in a MongoDB
* rpmcontroller --> Search rpms and take it to MongoDB
* rpmcontroller -f <pattern> --> Search RPMs in MongoDB
* debug mode --> log all actions in /var/log/rpmcontroller.log (Default deactivated)

Help:
```sh
Optional arguments:
  -h, --help            show this help message and exit
  -f pattern, --find pattern
                        Pattern to search in MongoDB
  -c, --check           Check if there are new rpms in node
  -d, --debug           Debug Mode
  --version             show program's version number and exit
```

License
----

MIT

*Free Software, Hell Yeah!*

  [Juan Manuel Parrilla]: juanmanuel.parrilla@amaris.com
  [@kerbeross]: http://twitter.com/@kerbeross
  [Francisco García Troitiño]: troitino@tid.es
  [1]: git@pdihub.hi.inet:troitino/rpmControler.git
  [Pymongo]: https://github.com/mongodb/mongo-python-driver
  [Argparse]: https://code.google.com/p/argparse
  
  
    
>>>>>>> test/concept
