rsync -Pav  hieradata/* /usr/local/rpmcontroller/puppet/hieradata/
rsync -Pav  modules/* /usr/local/rpmcontroller/puppet/modules
rsync -Pav  manifests/* /usr/local/rpmcontroller/puppet/manifests
mkdir -p /etc/facter/facts.d
rsync -Pav  /vagrant/pack/facter_smartM2M.yaml /etc/facter/facts.d/

puppet apply --environment rpmcontroller_pro_install --hiera_config /etc/puppet/hiera.yaml --modulepath=/usr/local/rpmcontroller/puppet/modules --debug  /usr/local/rpmcontroller/puppet/manifests/site.pp  --summarize
