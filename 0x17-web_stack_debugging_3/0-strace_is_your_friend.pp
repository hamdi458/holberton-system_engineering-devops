
# find out why Apache is returning a 500 error

exec { 'fix-wordpress':
path     => '/usr/local/bin/:/bin/',
cwd      => '/var/www/html/',
command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
provider => 'shell',
}