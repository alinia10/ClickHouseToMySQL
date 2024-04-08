# Use Ubuntu as the base image
FROM ubuntu:latest

# Set environment variables
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Install necessary system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libmysqlclient-dev \
    wget \
    git \
    htop \
    nano \
    bash \
# set default shell to bash
SHELL ["/bin/bash", "-c"]

# Install Docker
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
    && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
    && apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io \

# Install Docker Compose
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    docker-compose \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget -qO /tmp/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    /bin/bash /tmp/miniconda.sh -b -p /opt/conda && \
    rm /tmp/miniconda.sh

# Copy environment.yml
COPY environment.yml /tmp/environment.yml

# Set up Conda environment
RUN /opt/conda/bin/conda env create -f /tmp/environment.yml && \
    echo "source /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    conda init  && \
    echo "conda activate ana" >> ~/.bashrc

# Install setup.sh
COPY setup.sh /tmp/setup.sh
RUN /tmp/setup.sh

# Expose ports for other containers
EXPOSE 8123 9000 8888

# Start bash shell by default
CMD ["/bin/bash"]
