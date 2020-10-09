# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

exec { 'change os':
# hard
command  => "sudo sed -i 's/holberton hard nofile 5/holberton hard nofile 6000/g' /etc/security/limits.conf
# soft
sudo sed -i 's/holberton soft nofile 4/holberton soft nofile 6000/g' /etc/security/limits.conf",
provider => 'shell',
}