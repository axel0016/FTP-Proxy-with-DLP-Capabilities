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
## Basic Usage Instructions
You can input target addresses in the Web Nmap application either as a single IP address (e.g., 192.168.1.1), a range of IP addresses (e.g., 192.168.1.1-192.168.1.10), or a subnet (e.g., 192.168.1.0/24). For ports, you can specify individual ports (e.g., 22, 80, 443), a range (e.g., 1-1024), or leave it blank, in which case the application will scan the 1000 most common ports by default. You can select from several scan profiles, including SYN Scan (-sS) for stealthy scanning, TCP Connect Scan (-sT) for full TCP connections, UDP Scan (-sU) for UDP ports, and Intense Scan (-T4 -A -v) for detailed service, OS, and version detection. Other profiles include combinations of these scans, such as Intense Scan Plus UDP (-sS -sU -T4 -A -v) and Intense Scan, All TCP Ports (-p 1-65535 -T4 -A -v), as well as options like Quick Scan (-T4 -F), Quick Scan Plus (-sV -T4 -O -F -version-light), and Ping Scan (-sn) for quick host detection. You also have the option to input custom Nmap commands. Once the scan is initiated by clicking the “Scan” button, the results will appear in graphical form, showing a bar chart of open ports and hosts . The scan details will include host information, open ports, and versions, along with relevant CVEs (Common Vulnerabilities and Exposures) associated with the services found, providing you with valuable security insights. You can also export the results for further analysis.
