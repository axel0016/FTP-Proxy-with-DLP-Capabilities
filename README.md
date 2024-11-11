# Web Nmap Application Setup Guide using Docker

This guide provides a step-by-step process to install and run the **Web Nmap** application using Docker on **Ubuntu** or **Kali Linux**.

## Prerequisites

Ensure you have the following:
- A Debian-based Linux distribution (e.g., Ubuntu or Kali Linux)
- Administrative (sudo) privileges

## Steps

### 1. Update Your Package List

Run the following command to update your system's package list:

```bash
sudo apt update
```
### 2. Install Docker by running:
```bash
sudo apt install docker.io
```
### 3. Download the Web Nmap Docker Image
Pull the Docker image for the Web Nmap application:
```bash
sudo docker pull abdoumk/web_nmap:1.6
```
### 4. Run the Docker Container
Start the Docker container with host networking:
```bash
sudo docker run --network host abdoumk/web_nmap:1.6
```
### 5. Access the Application
Once the container is running, open a web browser and navigate to the machine’s IP address on port 5000:
```bash
http://<your-machine-host-ip>:5000
```
