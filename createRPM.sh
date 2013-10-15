mkdir -p BUILD RPMS SOURCES SPECS SRPMS
rm -rf /vagrant/rpmControler/RPMS/x86_64/*
/usr/bin/rpmbuild --buildroot `pwd`/BUILDROOT/ --define "_sourcedir `pwd`" --define "_rpmdir ./RPMS" --define "_buildir ." --define "_srcrpmdir ." --define "_speccdir ." --define "_topdir ." --define "_hash `date +%s`" --define "_jobs 01" --define "_changelog `date +%s`" -ba SPECS/rpmControler.spec
rm -f rpmControler-1.0.01-*.src.rpm
sudo rm -f /mnt/artifacts/others/rpmControler/rpmControler-1.0.01*
sudo cp /vagrant/rpmControler/RPMS/x86_64/* /mnt/artifacts/others/rpmControler/
#sudo createrepo /mnt/artifacts/others
