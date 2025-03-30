# Tools Used in Penetration Testing

This document provides an overview of the tools used in this penetration testing project, including installation, usage, and configuration details. The tools are categorized according to the penetration testing phases they are used in.

## 1. Burp Suite

### Purpose/Functionality:
Burp Suite is a comprehensive platform for web application security testing. It includes features for intercepting HTTP/S traffic, performing vulnerability scans, and identifying security weaknesses such as Cross-Site Scripting (XSS), SQL Injection, and other common web application vulnerabilities.

### Installation Instructions:
1. Download Burp Suite from the [official website](https://portswigger.net/burp).
2. Follow the installation instructions for your platform (Windows, macOS, Linux).
3. For Linux:
   ```bash
   wget https://portswigger.net/burp/releases/download?product=community&version=2021.7.2&type=Linux
   sudo dpkg -i burpsuite_community_v2021_7_2.deb

## Nmap

### Purpose/Functionality:
Nmap (Network Mapper) is a powerful open-source tool used for network discovery and security auditing. It is widely used for scanning ports, discovering network services, and identifying open ports and services running on a target system. It’s especially helpful in the **Reconnaissance** phase of penetration testing to gather information about a target system, including open ports, service versions, and the operating system.

### Installation Instructions:
1. Install Nmap from the official site or via package managers:
   - For Ubuntu:
     ```bash
     sudo apt-get install nmap
     ```
   - For macOS (Homebrew):
     ```bash
     brew install nmap
     ```

### Usage Instructions:
1. Basic scan to discover open ports on a target system:
   ```bash
   nmap -sS <target_ip>

