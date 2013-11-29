class fas3::params {

    if $caller_module_name != $module_name {
      fail("Use of private class ${name} by ${caller_module_name}")
    }

    $rpmcontroller_env=hiera('fas3')
	  $rpmcontroller_common_env=hiera('fas3_common')



    $path_to_repo_rpmcontroller=$rpmcontroller_env["path_to_repo_rpmcontroller"]
    #$path_to_ftp=$fas3_common_env["path_to_ftp"]
    #$path_to_fas3file=$fas3_common_env["path_to_fas3file"]

}
