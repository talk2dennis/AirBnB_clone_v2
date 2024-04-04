#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

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
ln -sf /data/web_static/releases/test/ /data/web_static/current

# give file ownership to ubuntu
chown -R ubuntu:ubuntu /data

# using alias to state the location of the static content for images
sudo sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default

# reload nginx
sudo service nginx restart
