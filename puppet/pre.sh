mkdir -p /usr/local/rpmcontroller/puppet/modules
mkdir -p /usr/local/rpmcontroller/puppet/manifests
mkdir -p /usr/local/rpmcontroller/puppet/hieradata
mkdir -p /etc/puppet/
mkdir -p /etc/puppet/facts.d/
                         
rsync -Pav modules/* /usr/local/rpmcontroller/puppet/modules                      
rsync -Pav  manifests/* /usr/local/rpmcontroller/puppet/manifests/                     
rsync -Pav hieradata/* /usr/local/rpmcontroller/puppet/hieradata/
rsync -Pav  pack/hiera.yaml /etc/puppet/
rsync -Pav  pack/facter_smartM2M.yaml /etc/puppet/facts.d/
ln -sf /usr/local/rpmcontroller/puppet/hieradata /var/lib/hiera
mkdir -p /var/lib/puppet/state
touch /var/lib/puppet/state/last_run_report.yaml

