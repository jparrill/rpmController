# == Class: rpmcontroller
#
# Module to install rpmcontroller.
#
# === Parameters
#
# Document parameters here.
#
# [*sample_parameter*]
#   N/A
# === Variables
#
# see hiera
#
#
# === Examples
#
#  class { rpmcontroller:
#  }
#
# === Authors
#
# Paco Troitino <troitino@tid.es>
#
# === Copyright
#
# Copyright 2013 TID
#
class rpmcontroller {
	class {'rpmcontroller::packages':}
	->
	class {'rpmcontroller::config':}
	->
	class {'rpmcontroller::service':}

}
