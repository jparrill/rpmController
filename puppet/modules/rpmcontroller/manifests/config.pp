class rpmcontroller::config inherits rpmcontroller::params{
  
    if $caller_module_name != $module_name {
      fail("Use of private class ${name} by ${caller_module_name}")
    } 

    File {
      seluser  => 'system_u',
      selrole  => 'object_r',
      seltype  => 'etc_t',
      selrange => 's0',
    }
    
    
    
	  file { 'config_rpmcontroler':
	    ensure 	=> file,
		  path	=> $path_to_config,
		  content => template('rpmcontroller/rpmController.erb'),    
    }
}