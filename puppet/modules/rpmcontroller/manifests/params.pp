class rpmcontroller::params {

    if $caller_module_name != $module_name {
      fail("Use of private class ${name} by ${caller_module_name}")
    }

    $path_to_repo_rpmcontroller=hiera('path_to_repo_rpmcontroller','http://artifacts.hi.inet/others/rpmController/6.X/x86_64/')
    $ip=hiera('ip','ci-rmtest.hi.inet')
    $port=hiera('port','27017')
    $database=hiera('databse','rpmdb')
    $path_to_config=hiera('path_to_config','/opt/rpmcontroller/conf/rpmController.ini')

}
