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
    
    
    
	  file { 'Default_ftp':
	    ensure 	=> file,
		  path	=> $path_to_ftp,
		  #require => Class['fas3::packages'],
		  content => template('fas3/Default_ftp.erb'),    
    }
}