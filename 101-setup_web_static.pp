# Puppet script that sets up your web servers for the deployment of web_static

package { 'nginx':
  ensure => installed,
}

file { '/data':
  ensure  => 'directory'
}

file { '/data/web_static':
  ensure => 'directory'
}

file { '/data/web_static/releases':
  ensure => 'directory'
}

file { '/data/web_static/releases/test':
  ensure => 'directory'
}

file { '/data/web_static/shared':
  ensure => 'directory'
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
}

file { '/var/www/html':
  ensure => 'directory'
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
    <p>Nginx server test</p>
  </body>
</html>"
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => "server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location /hbnb_static {
                alias /data/web_static/current;
        }
        error_page 404 /custom_404.html;

        # custom header
        add_header X-Served-By $hostname;

        location /redirect_me {

                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;

        }

}"
}

service { 'nginx':
  ensure => running,
}
