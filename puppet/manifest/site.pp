import 'nodes/*.pp'
notify {"M2M Managed Connectivity Initiative":}


Exec{
     logoutput => true,
}


define valor ($valor){
   notify {"${name} <===> ${valor}":}
}

define error {
  fail ("Variable ${name} no definida en: /etc/facter/facter.b/facter_smartM2M.yaml")
}

define warning{
  warning ("Variable ${name} no definida en: /etc/facter/facter.b/facter_smartM2M.yaml")
  warning ("Se asume que su valor es: true")
}

if $::version_smartm2m == undef
{
  error{"version_smartm2m":}
}
#else 
#{
#  valor{'version_smartm2m': valor => $::version_smartm2m}
#}

if $::installation_mode == undef
{
  error{"installation_mode":}
}
#else 
#{
#  valor{'installation_mode': valor => $::installation_mode}
#}

if $::smip == undef
{
  error{"smip":}
}
#else 
#{
#  valor{'smip': valor => $::smip}
#}

case $::puppet_manage_services {
    'yes': 
      { 
         $manage_services = true

      }
    undef: 
      { 
         warning{"manage_services":}
         $manage_services = true

      }
    'no': 
      { 
         $manage_services = false

      }
    default: { 
         $manage_services = false     
    }
 }

case $::puppet_manage_packages {
    'yes': 
      { 
         $manage_packages = true

      }
    undef: 
      { 
         warning{"manage_packages":}
         $manage_packages = true

      }
    'no': 
      { 
         $manage_packages = false

      }
    default: { 
         $manage_packages = false     
    }
}

case $::puppet_manage_config {
    'yes': 
      { 
         $manage_config = true

      }
    undef: 
      { 
         warning{"manage_config":}
         $manage_config = true

      }
    'no': 
      { 
         $manage_config = false

      }
    default: { 
         $manage_config = false     
    }
}

notify { "Variables":
    message  => "
    ##################################################################################
     
    VARIABLES:
    ##########
 
    \n version_smartm2m: ${::version_smartm2m} 
    \n installation_mode: ${::installation_mode} 
    \n smip: ${::smip} 
    \n manage_services: ${manage_services} 
    \n manage_packages: ${manage_packages} 
    \n manage_config: ${manage_config}
    
    ##################################################################################
    
    "
}



