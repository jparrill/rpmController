 
$ip="ci-rmtest.hi.inet"
$port="27017"
$database="rpmdb"
$path_to_config="/opt/rpmcontroller/conf/rpmController.ini"



if ( $::operatingsystemmajrelease == "6" )
{
  $path_to_repo_rpmcontroller="http://artifacts.hi.inet/others/rpmController/6.X/x86_64/"
}
else
{
  $path_to_repo_rpmcontroller="http://artifacts.hi.inet/others/rpmController/5.X/x86_64/"
}

File {
      seluser  => 'system_u',
      selrole  => 'object_r',
      seltype  => 'etc_t',
      selrange => 's0',
}
  

yumrepo { 'repo_rpmcontroller':
    descr    => 'Repo general del rpmcontroller',
    enabled  => 1,
    gpgcheck => 0,
    baseurl  => $path_to_repo_rpmcontroller,
    priority => 1,
   } 
->
exec { 'yum-clean-expire-cache':
    user => 'root',
    path => '/usr/bin',
    command => 'yum clean expire-cache',
  }
->
package { 'rpmcontroller':
  ensure  => latest,
  require => Yumrepo['repo_rpmcontroller'],
}    

