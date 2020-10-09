# failed requests. 
exec {'bring that limit higher':
path     => ['/usr/bin', '/bin'],
command  => "sudo sed -i 's/15/4096/g' /etc/default/nginx; sudo service nginx restart",
provider => 'shell',
}