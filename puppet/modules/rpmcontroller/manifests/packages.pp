class rpmcontroller::packages inherits rpmcontroller::params {

  if $caller_module_name != $module_name {
    fail("Use of private class ${name} by ${caller_module_name}")
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
  
}