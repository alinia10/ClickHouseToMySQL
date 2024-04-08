# Installation Guide

This guide will walk you through the steps to install Conda, create a Conda environment from an `environment.yml` file, and then install Docker Compose on Ubuntu.

## Step 1: Install Conda on Ubuntu
1. Open a terminal window.
2. Download the Miniconda installer script by running the following command:
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
3. Run the installer script by executing the following command:
```bash
bash Miniconda3-latest-Linux-x86_64.sh
```
4. Follow the prompts to complete the installation. Press `Enter` to scroll through the license agreement and type `yes` to accept the license.
5. Close the terminal window and open a new terminal window to activate the changes.
6. Verify that Conda was installed successfully by running the following command:
```bash
conda --version
```
## Step 2: Create a Conda environment from an `environment.yml` file
1. Navigate to the directory containing your `environment.yml` file.
2. Open a terminal window.
3. Create a Conda environment from the `environment.yml` file by running the following command:
```bash
conda env create -f environment.yml
```
2. Activate the Conda environment by running the following command:
```bash
conda activate ana
```
## Step 3: Install Docker and docker Compose

1. Open a terminal window.
2. Update the apt package index by running the following command:
```bash
sudo apt update
```
3. Install the required packages to allow apt to use a repository over HTTPS:
```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
4. Add Docker's official GPG key by running the following command:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
5. Add the Docker repository to the system's APT sources list:
```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```
6. Update the apt package index again:
```bash
sudo apt update
```
7. Install Docker by running the following command:
```bash
sudo apt install docker-ce
```
8. Start the Docker service and enable it to start on boot:
```bash
sudo systemctl start docker
sudo systemctl enable docker
```
9. Install Docker Compose by running the following command:
```bash
sudo apt install docker-compose
```
10. Verify that Docker Compose was installed successfully by checking the version:
```bash
docker-compose --version
```

## Run Docker compose
1. Navigate to the directory containing your `docker-compose.yml` file.
2. Open a terminal window.
3. Run the following command to start the Docker Compose services:
```bash 
docker-compose up -d
```
4. Wait for Docker Compose to download and start the services specified in the `docker-compose.yml` file.

## Conclusion

You have now successfully installed Conda, created a Conda environment from an `environment.yml` file, and installed Docker Compose on Ubuntu.
