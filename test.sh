#!bin/bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

apt-get -y install git docker-compose
systemctl restart docker.service

git clone https://github.com/GreenFrogSB/LMDS.git
cd LMDS/
sh deploy.sh
