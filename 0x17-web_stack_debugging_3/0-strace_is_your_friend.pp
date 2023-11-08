# fixes internal server error in apache by correcting the file extension from phpp to php in wp-setting.php
exec{'fix-wordpress':
        command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
        path    => '/usr/local/bin/:/bin/'
}
