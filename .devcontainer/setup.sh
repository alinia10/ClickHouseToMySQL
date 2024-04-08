# add docker group to sudoers
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

# run docker-compose
docker-compose ../docker-compose.yml -d
