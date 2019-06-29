# Atualização padrão
sudo apt update
sudo apt -y upgrade

# Clona a pasta do git que tem os script de client/server
git clone https://github.com/lucaspsacchi/Trab2-TAAD.git

# Baixando o docker e docker swarn
sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt -y install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
sudo systemctl enable docker

# Inicializando o docker swarm no master
sudo docker swarm init --advertise-addr 192.168.50.2:2377 | sed 5!d > /vagrant/token.sh

# Criação da rede
sudo docker network create -d overlay --subnet 10.0.10.0/24 ClusterNet

# Criação das imagens



# sudo docker service create --name server_service --network ClusterNet -p 5000:5000 server:latest
