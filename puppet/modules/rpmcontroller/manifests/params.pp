class rpmcontroller::params {

    if $caller_module_name != $module_name {
      fail("Use of private class ${name} by ${caller_module_name}")
    }

    $rpmcontroller_env=hiera('rpmcontroller')
	  $rpmcontroller_common_env=hiera('rpmcontroller_common')



    $path_to_repo_rpmcontroller=$rpmcontroller_env["path_to_repo_rpmcontroller"]
    $ip=$rpmcontroller_env["ip"]
    $port=$rpmcontroller_env["port"]
    $database=$rpmcontroller_common_env["databse"]
    $path_to_config=$rpmcontroller_common_env["path_to_config"]

}
