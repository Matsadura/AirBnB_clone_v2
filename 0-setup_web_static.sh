#!/usr/bin/env bash
# Sets up the web servers for the deployement of web_static

# Install Nginx if not already installed
if ! [[ -e  /usr/sbin/nginx ]]; then
	sudo apt-get -y install nginx
fi

# Create folders
FOLDERS=(/data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/)
for folder in "${FOLDERS[@]}"; do
	mkdir -p "$folder"
done

# Change ownership of data recursivly
chown -R ubuntu:ubuntu /data

# Remove sym link and recreate it
if [[ -L /data/web_static/current ]]; then
	rm /data/web_static/current
fi
ln -s /data/web_static/release/test/ /data/web_static/current

# Update Nginx configuration
sed -i "56i\ \tlocation /hbnb_static {\n \
\t\talias /data/web_static_/current/;\n\
\t}" /etc/nginx/sites-available/default

service nginx restart
