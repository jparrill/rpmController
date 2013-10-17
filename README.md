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


