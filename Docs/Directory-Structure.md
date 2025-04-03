# Project Directory Structure

This document outlines the directory structure of the Web Application Penetration Testing project. It serves as a guide to help users navigate the project and understand the purpose of each folder and file.

## Root Directory Overview

- **Docs/**: Documentation related to penetration testing methodologies, tools used, findings, and remediation guides.
  - **Methodology.md**: A detailed description of the penetration testing methodology employed in this project.
  - **Tools.md**: Information on the tools and technologies used for testing.

- **Findings/**: Contains the results of the penetration test, including vulnerability reports, exploitation evidence, and remediation guidelines.
  - **Vulnerabilities/**: Contains markdown files for each identified vulnerability. These files provide detailed descriptions and exploitation information for specific vulnerabilities (e.g., Broken Access Control, Cryptographic Failures).
  - **Evidence/**: Stores supporting evidence for findings, such as screenshots, logs, and proof-of-concept (PoC) scripts.
    - **Screenshots/**: Screenshots capturing evidence of vulnerabilities and exploitation.
    - **Logs/**: Logs documenting exploitation steps and test results.
    - **PoC Scripts/**: Proof of concept scripts demonstrating the vulnerability exploit.
  - **Remediation_Guides/**: Contains remediation advice for each vulnerability identified, including fixes and best practices.
  - **References/**: A collection of external references, such as CVEs, articles, and documentation relevant to the vulnerabilities.
  - **Findings.md**: A consolidated document summarizing the findings from the penetration test.

- **Reports/**: Contains the final penetration testing report, executive summary, and detailed findings with corresponding remediation steps.
  
- **Scripts/**: Stores automation scripts designed to assist in penetration testing, such as vulnerability scanning and exploitation tools.

- **juice-shop-setup.md**: A setup guide for deploying OWASP Juice Shop locally for testing purposes.

- **README.md**: The main entry point for understanding the project, its objectives, setup instructions, and usage details.

## Directory Tree

    Web-Application-Pentest-Project/
    ├── Docs/
    │   ├── Methodology.md
    │   ├── Tools.md
    ├── Findings/
    │   ├── Vulnerabilities/
    │   │   ├── A01:2021 - Broken-Access-Control.md
    │   │   ├── A02:2021 - Cryptographic-Failures.md
    │   │   ├── A03:2021 - Injection.md
    │   │   ├── A04:2021 - Insecure-Design.md
    │   │   ├── A05:2021 - Security-Misconfiguration.md
    │   │   ├── A06:2021 - Vulnerable-and-Outdated-Components.md
    │   │   ├── A07:2021 - Identification-and-Authentication-Failures.md
    │   │   ├── A08:2021 - Software-and-Data-Integrity-Failures.md
    │   │   ├── A09:2021 - Security-Logging-and-Monitoring-Failures.md
    │   │   ├── A10:2021 - Server-Side-Request-Forgery(SSRF).md
    │   ├── Evidence/
    │   │   ├── Screenshots/
    │   │   ├── Logs/
    │   │   ├── PoC Scripts/
    │   ├── Remediation_Guides/
    │   │   ├── A01:2021 - Broken-Access-Control.md
    │   │   ├── A02:2021 - Cryptographic-Failures.md
    │   │   ├── A03:2021 - Injection.md
    │   │   ├── A04:2021 - Insecure-Design.md
    │   │   ├── A05:2021 - Security-Misconfiguration.md
    │   │   ├── A06:2021 - Vulnerable-and-Outdated-Components.md
    │   │   ├── A07:2021 - Identification-and-Authentication-Failures.md
    │   │   ├── A08:2021 - Software-and-Data-Integrity-Failures.md
    │   │   ├── A09:2021 - Security-Logging-and-Monitoring-Failures.md
    │   │   ├── A10:2021 - Server-Side-Request-Forgery(SSRF).md
    │   ├── References/
    │   ├── Findings.md
    ├── Reports/
    ├── Scripts/
    ├── juice-shop-setup.md
    └── README.md


## Detailed Folder Description

### `Docs/`
This folder holds all documentation files.
- **Methodology.md**: Details the penetration testing approach, including reconnaissance, scanning, exploitation, and post-exploitation techniques.
- **Tools.md**: Lists the tools and technologies used during the penetration test, with explanations of their purpose and usage.

### `Findings/`
This folder includes all findings from the penetration test, organized as follows:
- **Vulnerabilities/**: Each markdown file corresponds to a specific vulnerability identified during the test (e.g., Broken Access Control, Cryptographic Failures). These files detail the nature of the vulnerability and how it was discovered.
- **Evidence/**: Contains evidence that supports the findings.
  - **Screenshots/**: Visual proof of vulnerabilities or exploitation attempts.
  - **Logs/**: Logs that document the testing process and exploitation steps.
  - **PoC Scripts/**: Scripts demonstrating proof of concept for the vulnerabilities.
- **Remediation_Guides/**: Detailed recommendations and fixes for each identified vulnerability.
- **References/**: Relevant external documentation, including CVE links, OWASP resources, and other industry standards.

### `Reports/`
This folder contains the final deliverables of the penetration testing engagement:
- **Pentest Report**: A comprehensive report summarizing findings, risks, and remediation advice.
- **Findings Summary**: An executive summary for stakeholders.

### `Scripts/`
Automation scripts used to conduct penetration testing and vulnerability scans.

### `juice-shop-setup.md`
A guide to set up the OWASP Juice Shop application locally for testing and training.

### `README.md`
Provides an overview of the project, instructions for setup, and how to use the resources in the repository.

## Notes
- **Findings** is the primary folder for in-depth information on vulnerabilities, exploitation, and remediation.
- **Reports** is where the final penetration testing report and summary of findings reside.
- **Scripts** contains automation tools that streamline testing tasks.

This structure is designed to provide clear organization for efficient workflow and ease of access to important resources in the penetration testing process.


