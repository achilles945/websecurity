# OWASP Juice Shop Setup using Docker on Parrot OS

This guide will help you set up **OWASP Juice Shop** using **Docker** on your Parrot OS machine.

## 1. Install Docker on Parrot OS

### Step 1: Update Your Package List
Open a terminal and update your system’s package list:

```bash
sudo apt update
```

### Step 2. Install Required Packages

```bash 
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

### Step 3. Add Docker's Official GPG key

```bash
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

### Step 4: Add Docker's Official Repository

```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### Step 5: Update Package List Again

```bash
sudo apt update
```

### Step 6: Install Docker Engine

```bash
sudo apt install docker-ce docker-ce-cli containerd.io
```

### Step 7: Verify Docker Installation

1. Check if Docker is installed and running

```bash
sudo systemctl status docker
```

2. If not running, start it using

```bash
sudo systemctl start docker
```

---

## 2 Pull the OWASP Juice Shop Docker Image

### Command

```bash
sudo docker pull owasp/juice-shop
```

---

## 3 Run OWASP Juice Shop in Docker

1. Run juice shop

```bash
sudo docker run -d -p 3000:3000 owasp/juice-shop
```

``-d``: Run container in background <br>
``-p 3000:300``: Maps port 3000 on your local machine to port 3000 inside the container.

2. Verify Container is Running

```bash
sudo docker ps
```

## 4 Access OWASP Juice Shop

1. Type this URL in your browser

```arduino
http://localhost:3000
```

## 5 Stop and Remove the Container

After you are done with Juice Shop you can stop or remove it 

1. find container ID

```bash
sudo docker ps
```

2. Stop Juice Shop Container:

```bash
sudo docker stop <container_id_or_name>
```

3. Remove the Container

```bash
sudo docker rm <container_id_or_name>
```
