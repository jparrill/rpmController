%define _base RpmControles
%define _psdir /opt/pdi/rpmControler/


Name:           %{_base}
Version:        1.0.%{_jobs}
Release:        %{_hash}
Summary:       Instalation of rpmControler (RE) 
BuildArch: x86_64
SOURCE0: %{_topdir}/SOURCES
Group:         PDI/rpmControler 
License:       GNU Affero V3 (see LICENSE file)
URL:           http://www.tid.es
Vendor:        Telefonica PDI 
BuildRoot: %{_topdir}/BUILD/%{name}
Provides: %{_base}
Requires: nodejs => 0.8

%description

Es un programa hecho en python que almacena en una bbdd de mongodb los paquetes instalados en la maquina a lo largo del tiempo.

%prep

%build

%pre
if [ "$1" = "1" ] 
then
  # Perform tasks to prepare for the initial installation
	#Create group perserver if not exists
	OSUSER=rpm_controler
	OSGROUP=rpm_controler
	/bin/grep "^$OSGROUP" /etc/group > /dev/null 2>&1
	if [ $? != 0 ]
	then
	  /usr/sbin/groupadd -r -f $OSGROUP
	  if [ $? != 0 ]
	  then
	    echo "Problems creating group $OSGROUP. Exiting."
	    exit -1
	  fi
	fi
	#Create user push_server
	/usr/bin/id $OSUSER > /dev/null 2>&1
	if [ $? != 0 ]
	then
	  /usr/sbin/useradd -d %{_psdir} -g $OSGROUP -M -r -s /bin/bash  $OSUSER
	  if [ $? != 0 ]
	  then
	    echo "Problems creating user $OSUSER. Exiting."
	    exit -1
	  fi
	fi
fi

%install
rm -rf $RPM_BUILD_ROOT
if [ ! -d $RPM_BUILD_ROOT%{_psdir} ]
then
  mkdir -p $RPM_BUILD_ROOT%{_psdir}
fi

cp -r %SOURCE0/. $RPM_BUILD_ROOT%{_psdir}



%clean
rm -rf $RPM_BUILD_ROOT


%post
if [ "$1" = "1" ] 
then
  # Perform tasks to prepare for the initial installation
  if [ ! -f /etc/init.d/pushserverd ]
  then
    ln -s %{_psdir}/src/pushserverd /etc/init.d/pushserverd
  fi
fi
if [ ! -d /var/log/push_server/ ]
then
  mkdir -p /var/log/push_server/
fi
if [ ! -f /etc/logrotate.d/push_server.conf ]
then
  cp %{_psdir}/other/logrotate/push_server.conf /etc/logrotate.d/
fi

%postun
if [ $1 -eq 0 ]; then
  # Perform tasks to prepare for the initial uninstallation
  unlink /etc/init.d/pushserverd
  rm -f /etc/logrotate.d/push_server.conf
fi
%files
%defattr(755,rpm_controler,rpm_controler,-)
%dir %{_psdir}/
%{_psdir}/*

%changelog
