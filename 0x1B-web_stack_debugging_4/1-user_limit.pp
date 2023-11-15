# Allows the holberton user to login and open a file without any error message.
# Increases the hard and soft limits

exec { 'set holberton user hard limit':
  command => "/bin/sed -i '/^holberton hard /s/4/4096/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}

exec { 'set holberton user soft limit':
  command => "/bin/sed -i '/^holberton soft /s/5/4096/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}
