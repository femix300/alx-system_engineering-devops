# installs and configures nginx on a server
package { 'nginx':
  ensure => 'installed',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => '
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  server_name _;

  location / {
    root /var/www/html;
    index index.html;
    try_files $uri $uri/ =404;
  }

  location = /redirect_me {
    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
  }
}
',
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => "Hello World!\n",
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
