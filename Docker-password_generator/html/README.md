# Password-generator
Генерация паролей с помощью псевдослучайной последовательности из /dev/urandom

## Installation
Install LAMP Server on Ubuntu 16.04 and more..

```sh
sudo apt update

sudo apt install -y software-properties-common python-software-properties

sudo add-apt-repository ppa:ondrej/php

sudo apt install -y apache2 apache2-doc apache2-utils libexpat1 ssl-cert
sudo apt install -y libapache2-mod-php7.2 php7.2 php7.2-common php7.2-curl php7.2-dev php7.2-gd php-pear php-imagick php7.2-mcrypt php7.2-mysql php7.2-ps php7.2-xsl

sudo update-alternatives --set php /usr/bin/php7.2 && sudo a2enmod php7.2 && sudo systemctl restart apache2

sudo chown -R www-data:www-data /var/www
sudo usermod -aG root,www-data ubuntu
sudo usermod -aG root,www-data student
sudo chmod -R 777 /var/www
```
