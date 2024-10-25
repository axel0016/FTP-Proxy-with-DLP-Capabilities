# FTP Proxy with DLP

This project is an FTP Proxy server with basic Data Loss Prevention (DLP) capabilities. It monitors file uploads, checks for sensitive content, and forwards or blocks files based on the results.

## Features
- **FTP Proxy:** Acts as an intermediary server to handle FTP requests.
- **DLP Checks:** Scans uploaded files for sensitive content using keyword matching.
- **Custom Login:** Prompts for real server credentials via a graphical interface.
- **File Blocking:** Blocks sensitive files and forwards allowed files to a real server.
- **Alerts:** Displays alerts via message boxes for key actions.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/ftp-proxy-dlp.git
cd ftp-proxy-dlp
pip install pyftpdlib

## Usage
1. Connect to the server using an FTP client on port `2121`.
2. Enter the real server’s credentials when prompted.
3. Files containing sensitive content are blocked, and others are forwarded to the specified FTP server.
