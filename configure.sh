#!/bin/bash

#RUN WITH SUDO


dnf install httpd python mysql-server python3.12 python3.12-pip -y

pip3 install fastapi[standard]

mkdir -p /usr/api/
mkdir -p /var/www/vhosts/search/
mkdir -p /var/log/fastapi/

systemctl enable --now mysqld

mysql -e "UPDATE mysql.user SET Password = PASSWORD('Passw0rd!') WHERE User = 'root'"
# Kill the anonymous users
mysql -e "DROP USER ''@'localhost'"
# Because our hostname varies we'll use some Bash magic here.
mysql -e "DROP USER ''@'$(hostname)'"
# Kill off the demo database
mysql -e "DROP DATABASE test"
# Make our changes take effect
mysql -e "FLUSH PRIVILEGES"
# Any subsequent tries to run queries this way will get access denied because lack of usr/pwd param
mysql -e "CREATE DATABASE search;"

mysql -e "CREATE TABLE key_data(key_id VARCHAR(50), url VARCHAR(250), PRIMARY KEY (key));"

mysql -e "CREATE TABLE log(key_id VARCHAR(50), searched INT, PRIMARY KEY (key_id));"

mysql -e "CREATE USER 'python'@'%';"

mysql -e "GRANT ALL PRIVILEGES ON search.* TO 'python'@'%';"


mv ./python/fastapi.service /etc/systemd/system/ 
mv ./httpd/vhosts.conf /etc/httpd/conf.d/
mv -r ./httpd/search /var/www/vhosts/
mv -r ./python/ /usr/api/ 

systemctl daemon-reload
systemctl enable --now fastapi
systemctl enable --now httpd



