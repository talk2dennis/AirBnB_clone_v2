#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Define the hostname variable
hostname=$(hostname)


# html content
page="\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

sudo apt -y update
sudo apt -y install nginx

# create the necessary folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# create fake html file 
echo "$page" | sudo tee "/data/web_static/releases/test/index.html" > "/dev/null"

# check if file exists and delete
#if [ -f /data/web_static/current ]; then
#	rm /data/web_static/current
#fi

# create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# give file ownership to ubuntu
chown -R ubuntu:ubuntu /data

# using alias to state the location of the static content for images
sudo printf %s "\
server {
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

}" > /etc/nginx/sites-available/default

# reload nginx
sudo service nginx restart
