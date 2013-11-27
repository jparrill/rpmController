<<<<<<< HEAD
rpmContoler
==========

Description
===========

Programa hecho en python que permite llevar un historico de los paquetes (rpms) instalados en las maquinas.

La información que se guarda es:

Información de la maquina:
- Nombre maquina
- Ips
- date
- system
- release
- version
- distribution

Información de los rpms de cada maquina:
- nombre del rpm
- date_process
- date_installed

Contiene dos programas.

rpmControler.py
---------------

Se encarga de realizar el control de los rpms.

Se instala en el contrab y se ejecuta cada 10 minutos. 

rpmFind.py
----------

Realiza las consultas.

Ejemplo:

Busqueda por ip de la maquina.

./rpmFind.py -i 

Busqueda por el nombre de la maquina

./rpmFind.py -h

Busqueda por nombre de la maquina, solo muestra la información relativa al host

./rpmFind.py -o

Busqueda por nombre de la maquina, solo muestra la información relativa a los rpms.

./rpmFind.py -r

Muestra todos los hots que estan siendo controlados.

./rpmFind.py -A


BBDD:
-----

La información se guarda en un servidor mongo centralizado.


INSTALACIOM
===========

Crear el reositorio rpmCrontoler.repo

vi /etc/yum.repos.d/rpmControler.repo
[rpmControler]
name=rpmControler
baseurl=http://artifacts.hi.inet/others/rpmControler/
enabled=1
gpgcheck=0
priority=1

Ejecutar:
yum -y install rpmControler 


=======
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
