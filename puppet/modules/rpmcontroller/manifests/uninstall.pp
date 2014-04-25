
class rpmcontroller::uninstall inherits rpmcontroller::params {


  Package{
    ensure => absent
  }

  File{
    ensure => absent
  }
  
  

  notify {"WARNING: Uninstalling the module rpmcontroller":}
  ->
  #Cuidado: No es un servicio esta en el cron
  service { 'rpmcontroller':
    ensure    => stopped,
    enable    => false,
  }
  ->
  package { 'rpmcontroller':}
  ->
  file { 'config_rpmcontroler':
      path  => $path_to_config,
  ->
  file { 'contrab_rpmcontroler':
      path  => '/etc/cron.hourly/rpmController',
  ->
  file { 'repo_rpmcontroller':
    path  => '/etc/yum.repos.d/repo_rpmcontroller.repo',
  }
  ->
  exec { 'yum-clean-expire-cache':
      user => 'root',
      path => '/usr/bin',
      command => 'yum clean expire-cache',
    }
  
}