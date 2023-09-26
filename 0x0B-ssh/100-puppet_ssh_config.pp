#!/usr/bin/env bash
# A puppet manifest to make changes to an ssh configuration file
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => 'Host *
    HostName 3.83.18.144
    User ubuntu
    PasswordAuthentication no
    IdentityFile ~/.ssh/school
  ',
}
