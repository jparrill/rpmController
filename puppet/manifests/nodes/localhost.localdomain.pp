node 'localhost.localdomain' {
    
    notify {"${::version_rpmcontroller} ${::installation_mode}":}

    

    case $::installation_mode {
    rollforward: 
      { 
        class { 'rpmcontroller': }
      }
    rollback:
      {
        class { 'rpmcontroller::uninstall': } 
      }
    default: { fail("Unreconginzed installation mode")}
    }

}
