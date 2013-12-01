node 'dev-owd-pushserver-01.hi.inet' {
    
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