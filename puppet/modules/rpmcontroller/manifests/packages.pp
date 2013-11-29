class rpmcontroller::packages inherits rpmcontroller::params {

  if $caller_module_name != $module_name {
    fail("Use of private class ${name} by ${caller_module_name}")
  }

   
  
  yumrepo { 'repogeneral':
    descr    => 'Repo general de M2M Portal',
    enabled  => 1,
    gpgcheck => 0,
    baseurl  => $path_to_repo_rpmcontroller,
    priority => 1,
   }

  package { 'rpmcontroller':
    ensure  => latest,
    require => Yumrepo['repogeneral'],
  }
  
}