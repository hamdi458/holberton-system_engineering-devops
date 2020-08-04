# Connect without pasword
exec { 'echo "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no" >> /etc/ssh/ssh_config':
  path  => '/bin/'
}