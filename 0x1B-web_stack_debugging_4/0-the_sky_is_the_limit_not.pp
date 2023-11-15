# Increases the ULIMIT
exec { 'increase ulimit':
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'restart nginx':
    command => '/etc/init.d/nginx restart',
    path    => '/etc/init.d/'
}
