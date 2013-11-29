node 'localhost.localdomain' {
    
    notify {"${::version_smartm2m} ${::installation_mode}":}

    case $::version_smartm2m {
    '2.1.0': {
            notify {'Estoy en la versión 2.1.0':}
         }
    '2.2.0': {
            notify {'Estoy en la versión 2.2.0':}
         }
    '2.3.0': {
            notify {'Estoy en la versión 2.3.0':}
         }
    default: { fail("Unreconginzed version of smartM2M")}
    }

    case $::installation_mode {
    rollforward: 
      { 
        class { 'security': } ->
        class { 'be_base': } ->
        class { 'memcache': } ->
        class { 'be': } ->
        class { 'fe': } ->
        class { 'navision': }
        #class {'async_base':} 

      }
    rollback:
      {
        class { 'navision::uninstall':}
        ->
        class { 'be::uninstall':}
        ->
        class { 'fe::uninstall':}
        ->
        class { 'async_base::uninstall':}
        ->
        class { 'memcache::uninstall':}
        ->
        class { 'be_base::uninstall':}
        ->
        class { 'security::uninstall':}
        #class { 'fas3::uninstall': } 
      }
    default: { fail("Unreconginzed installation mode")}
    }

}
