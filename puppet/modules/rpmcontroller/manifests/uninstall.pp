
class fas3::uninstall inherits fas3::params {


  Package{
    ensure => absent
  }

  File{
    ensure => absent
  }
  
  notify {"Cambio hecho por paco":}

  notify {"WARNING: Uninstalling the module fas3":}
  ->
  #Cuidado: No es un servicio esta en el cron
  service { 'm2m-fas3':
    ensure    => stopped,
    enable    => false,
  }
  ->
  package { 'm2m-fas3':}
  ->
  file { 'Default_ftp':
    path  => $path_to_ftp,
  }
  ->
  file { 'Default_generatefas3file':
    path	=> $path_to_fas3file,
  }
  ->
  # en vez de hacer un yumrepo repogeneral ensure absent borra el fichero directamente.
  file { 'repogeneral':
    path  => '/etc/yum.repos.d/repogeneral.repo',
  }
  ->
  exec { 'yum-clean-expire-cache':
      user => 'root',
      path => '/usr/bin',
      command => 'yum clean expire-cache',
    }
  
}