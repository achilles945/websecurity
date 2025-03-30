# 🛡️ Web Application Penetration Testing Project

## 📌 Introduction  
This project focuses on conducting a **penetration test** on the **OWASP Juice Shop** web application, following the **PTES (Penetration Testing Execution Standard)** methodology as the primary framework. Additionally, the **OWASP WSTG (Web Security Testing Guide)** is integrated within the process, and the **OWASP Top 10 vulnerabilities** are exploited during the testing. The repository includes:  
✔️ A structured **pentesting methodology**  
✔️ Automated **testing scripts**  
✔️ Detailed **vulnerability reports**  
✔️ **Proof-of-concept** screenshots  
✔️ **Remediation guides** for security fixes  

---

## 📂 Table of Contents  
- [Scope](#scope)  
- [Methodology](#methodology)  
- [Tools Used](#tools-used)  
- [Findings](#findings)  
- [Reports](#reports)  
- [Usage Instructions](#usage-instructions)  
- [Folder Structure](#folder-structure)  
- [Contributing](#contributing)  
- [Disclaimer](#disclaimer)  

---

## 🎯 Scope  
- **Target:** OWASP Juice-Shop  
- **Testing Approach:** **Black-box**  
- **Vulnerabilities Covered:**  
  - **OWASP Top 10 (2021)**  
  - **Additional security misconfigurations**  
- **Testing Environment:** **Local**  

---

## 🛠️ Methodology  
This penetration test follows the **PTES methodology** as the primary approach, with integration of the **OWASP Web Security Testing Guide (WSTG)**. The methodology consists of:

1. **Intelligence Gathering** – Information gathering (subdomains, technologies, endpoints).  
2. **Vulnerability Analysis** – Identifying exposed services and vulnerabilities.  
3. **Exploitation** – Running attacks using scripts & manual techniques, exploiting OWASP Top 10 vulnerabilities.
4. **Post-Exploitation** – Assessing data exposure & privilege escalation.  
5. **Reporting & Remediation** – Documenting findings and recommending fixes.  

Additionally, this test leverages the **OWASP WSTG** guidelines for thorough and comprehensive security assessments.

📖 Detailed methodology can be found in **[Docs/Methodology.md](Docs/Methodology.md)**.  

---

## 🛠️ Tools Used  
The following tools were used for testing:  
- **Reconnaissance:** `Nmap`  
- **Scanning:** `Nikto, Dirb, Gobuster, Burp Suite`  
- **Exploitation:** `SQLmap, Metasploit, Custom Scripts`  
- **Post-Exploitation:** `Mimikatz, Hashcat`  

---

## 🔍 Findings  
Identified vulnerabilities include:  
- ✅ **A01 – Broken Access Control** _(Privilege escalation, IDOR)_  
- ✅ **A03 – SQL Injection** _(Database extraction, authentication bypass)_  
- ✅ **A07 – Identification & Authentication Failures** _(Weak passwords, session hijacking)_  

📂 For a detailed breakdown, check **[Findings/](Findings/)**.  

---

## 📊 Reports  
- 📄 **Pentest Report:** [Reports/OWASP_Top_10_Pentest_Report.pdf](Reports/OWASP_Top_10_Pentest_Report.pdf)  
- 📊 **Findings Summary:** [Reports/Vulnerability-Findings.xlsx](Reports/Vulnerability-Findings.xlsx)  
- 🛠️ **Fixing Issues:** [Reports/Remediation_Guide.md](Reports/Remediation_Guide.md)  

---

## 🚀 Usage Instructions  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/Web-Application-Pentest-Project.git
   cd Web-Application-Pentest-Project
