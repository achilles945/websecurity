# 🛡️ Web Application Penetration Testing Project  

#### **⚠️ This project is currently in development. Some features and documentation may be incomplete. ⚠️**


## Introduction  
This project focuses on conducting a **penetration test** on the **OWASP Juice Shop** web application, following the **OWASP WSTG (Web Security Testing Guide)** methodology as the primary framework. Additionally, the **OWASP Top 10 vulnerabilities** are exploited during the testing. <br>
**The repository includes**: <br>
✔️ A structured **pentesting methodology**  
✔️ Automated **testing scripts**  
✔️ Detailed **vulnerability reports**  
✔️ **Proof-of-concept** screenshots  
✔️ **Remediation guides** for security fixes  

---

## Table of Contents  
- [Scope](#Scope)  
- [Methodology](#Methodology)  
- [Tools Used](#Tools-Used)  
- [Findings](#Findings)  
- [Reports](#Reports)  
- [Directory Structure](#Directory-Structure)  
- [Usage Instructions](#Usage-Instructions)   

---

## Scope  
- **Target:** OWASP Juice-Shop  
- **Testing Approach:** **Black-box**  
- **Vulnerabilities Covered:**  
  - **OWASP Top 10 (2021)**    
- **Testing Environment:** **Local**  

---

## Methodology  
This penetration test follows the **OWASP Web Security Testing Guide (WSTG)** Methodology. The WSTG is a comprehensive guide to testing the security of web applications and web services, it provides a framework of best practices used by penetration testers and organizations <br>

**The methodology consists of**:

1. **Information Gathering**: Collect detailed information about the target to identify potential attack vectors.
2. **Vulnerability Identification (Scanning & Security Testing)**: Identify vulnerabilities within the web application by testing common attack vectors.
3. **Exploiting Vulnerabilities (Proof of Concept)**: Test identified vulnerabilities to confirm their exploitability.
4. **AReporting & Remediation**: Document findings, explain the impact of vulnerabilities, and provide remediation steps.

This test leverages the **OWASP WSTG** guidelines for thorough and comprehensive security assessments.

📖 Detailed methodology can be found in **[docs/methodology.md](docs/methodology.md)**.  

---

## Tools Used  
The following tools were used for testing:  
- **Information Gathering:** `Nmap, Nikto, Wget, Shodan`  
- **Vulnerability Identification (Scanning & Security Testing):** `Nikto, ZAP, Burp Suite`  

📖 Detailed tools information can be found in **[docs/tools.md](docs/tools.md)**.  

---

## Findings  
Identified vulnerabilities include:  
- ✅ **A01 – Broken Access Control** _(Privilege escalation, IDOR)_  
- ✅ **A03 – SQL Injection** _(Database extraction, authentication bypass)_ 
- ✅ **A05 - Security Misconfiguration** _(Improperly configured permissions, Default Credentials)_
- ✅ **A07 – Identification & Authentication Failures** _(Weak passwords, session hijacking)_  

📂 For a detailed breakdown, check **[findings/](findings/)**.  

---

## Reports  
- 📄 **Pentest Report:** [reports/OWASP_Top_10_Pentest_Report.pdf](reports/OWASP_Top_10_Pentest_Report.pdf)  
- 📊 **Findings Summary:** [reports/Vulnerability-Findings.xlsx](reports/Vulnerability-Findings.xlsx)  
- 🛠️ **Fixing Issues:** [reports/Remediation_Guide.md](reports/Remediation_Guide.md)  

---

## Project Directory Structure

The project is organized into several directories to maintain clarity and structure. Below is a brief overview of the key folders and their contents:

- **Docs/**: Contains documentation related to the penetration testing process.
  - **Methodology.md**: Detailed penetration testing methodology.
  - **Tools.md**: Information on the tools used in the testing.

- **Findings/**: Contains reports and evidence of vulnerabilities identified during testing.
  - **Vulnerabilities/**: Vulnerability reports with detailed exploitation information.
  - **Evidence/**: Supporting evidence like screenshots, logs, and proof-of-concept scripts.
  - **Remediation_Guides/**: Guides to remediate each identified vulnerability.
  - **Findings.md**: A summary of all findings.

- **Reports/**: Contains the final penetration testing report and executive summaries.

- **Scripts/**: Holds automated testing scripts for penetration testing tasks.

- **juice-shop-setup.md**: Instructions for setting up the OWASP Juice Shop for local testing.

- **README.md**: The main entry point for understanding the project, its objectives, and setup instructions.

📖 Detailed Directory-Structure can be found in **[docs/directory-structure.md](docs/directory-structure.md)**.

---

## Usage Instructions  
1. Clone the repository:  
   ```bash
   git clone https://github.com/achilles945/Web-Application-Pentest-Project.git
   cd Web-Application-Pentest-Project
