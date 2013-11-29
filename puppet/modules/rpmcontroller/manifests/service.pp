class fas3::service {
  
  if $caller_module_name != $module_name {
    fail("Use of private class ${name} by ${caller_module_name}")
  }
    
  #if $manage_services
  #{
  #     realize ( File['Default_ftp'],File['Default_generatefas3file'] )
  #}
	#service { 'm2m-fas3':
	#	ensure 		=> running,
	#	enable 		=> true,
	#	hasrestart 	=> true,
	#	require 	=> Class['fas3::config']
	#}
}