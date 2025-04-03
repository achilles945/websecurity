# 🛡️ Web Application Penetration Testing Project  

#### **⚠️ This project is currently in development. Some features and documentation may be incomplete. ⚠️**


## 📌 Introduction  
This project focuses on conducting a **penetration test** on the **OWASP Juice Shop** web application, following the **OWASP WSTG (Web Security Testing Guide)** methodology as the primary framework. Additionally, the **OWASP Top 10 vulnerabilities** are exploited during the testing. <br>
**The repository includes**: <br>
✔️ A structured **pentesting methodology**  
✔️ Automated **testing scripts**  
✔️ Detailed **vulnerability reports**  
✔️ **Proof-of-concept** screenshots  
✔️ **Remediation guides** for security fixes  

---

## 📂 Table of Contents  
- [Scope](#Scope)  
- [Methodology](#Methodology)  
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
- **Testing Environment:** **Local**  

---

## 🛠️ Methodology  
This penetration test follows the **OWASP Web Security Testing Guide (WSTG)** Methodology. The WSTG is a comprehensive guide to testing the security of web applications and web services, it provides a framework of best practices used by penetration testers and organizations <br>

**The methodology consists of**:

1. **Information Gathering**: 
2. **Configuration and Deployment Management Testing**: 
3. **Identity Management Testing**: 
4. **Authentication Testing**: 
5. **Authorization Testing**: 
6. **Session Management Testing**: 
7. **Input Validation Testing**: 
8. **Testing for Error Handling**: 
9. **Testing for Weak Cryptography**: 
10. **Business Logic Testing**: 
11. **Client-side Testing**: 

This test leverages the **OWASP WSTG** guidelines for thorough and comprehensive security assessments.

📖 Detailed methodology can be found in **[Docs/Methodology.md](Docs/Methodology.md)**.  

---

## 🛠️ Tools Used  
The following tools were used for testing:  
- **Information Gathering:** `Nmap, Nikto, Wget`  
- **Security Assessment:** `Nikto, ZAP, Burp Suite`  

---

## 🔍 Findings  
Identified vulnerabilities include:  
- ✅ **A01 – Broken Access Control** _(Privilege escalation, IDOR)_  
- ✅ **A03 – SQL Injection** _(Database extraction, authentication bypass)_ 
- ✅ **A05 - Security Misconfiguration** _(Improperly configured permissions, Default Credentials)_
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
