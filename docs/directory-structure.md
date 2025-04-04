# Project Directory Structure

This document outlines the directory structure of the Web Application Penetration Testing project. It serves as a guide to help users navigate the project and understand the purpose of each folder and file.

## Root Directory Overview

- **docs/**: Documentation related to penetration testing methodologies, tools used, findings, and remediation guides.
  - **methodology.md**: A detailed description of the penetration testing methodology employed in this project.
  - **tools.md**: Information on the tools and technologies used for testing.

- **findings/**: Contains the results of the penetration test, including vulnerability reports, exploitation evidence, and remediation guidelines.
  - **vulnerabilities/**: Contains markdown files for each identified vulnerability. These files provide detailed descriptions and exploitation information for specific vulnerabilities (e.g., Broken Access Control, Cryptographic Failures).
  - **evidence/**: Stores supporting evidence for findings, such as screenshots, logs, and proof-of-concept (PoC) scripts.
    - **screenshots/**: Screenshots capturing evidence of vulnerabilities and exploitation.
    - **logs/**: Logs documenting exploitation steps and test results.
    - **poc-scripts/**: Proof of concept scripts demonstrating the vulnerability exploit.
  - **remediation-guides/**: Contains remediation advice for each vulnerability identified, including fixes and best practices.
  - **references/**: A collection of external references, such as CVEs, articles, and documentation relevant to the vulnerabilities.
  - **findings.md**: A consolidated document summarizing the findings from the penetration test.

- **reports/**: Contains the final penetration testing report, executive summary, and detailed findings with corresponding remediation steps.
  
- **scripts/**: Stores automation scripts designed to assist in penetration testing, such as vulnerability scanning and exploitation tools.

- **juice-shop-setup.md**: A setup guide for deploying OWASP Juice Shop locally for testing purposes.

- **README.md**: The main entry point for understanding the project, its objectives, setup instructions, and usage details.

## Directory Tree

    Web-Application-Pentest-Project/
    ├── docs/
    │   ├── methodology.md
    │   ├── tools.md
    ├── findings/
    │   ├── vulnerabilities/
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
    │   ├── evidence/
    │   │   ├── screenshots/
    │   │   ├── logs/
    │   │   ├── poc-scripts/
    │   ├── remediation-guides/
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
    │   ├── references/
    │   ├── findings.md
    ├── reports/
    ├── scripts/
    ├── juice-shop-setup.md
    └── README.md


## Detailed Folder Description

### `docs/`
This folder holds all documentation files.
- **methodology.md**: Details the penetration testing approach, including reconnaissance, scanning, exploitation, and post-exploitation techniques.
- **tools.md**: Lists the tools and technologies used during the penetration test, with explanations of their purpose and usage.

### `findings/`
This folder includes all findings from the penetration test, organized as follows:
- **vulnerabilities/**: Each markdown file corresponds to a specific vulnerability identified during the test (e.g., Broken Access Control, Cryptographic Failures). These files detail the nature of the vulnerability and how it was discovered.
- **evidence/**: Contains evidence that supports the findings.
  - **screenshots/**: Visual proof of vulnerabilities or exploitation attempts.
  - **logs/**: Logs that document the testing process and exploitation steps.
  - **poc-scripts/**: Scripts demonstrating proof of concept for the vulnerabilities.
- **remediation-guides/**: Detailed recommendations and fixes for each identified vulnerability.
- **references/**: Relevant external documentation, including CVE links, OWASP resources, and other industry standards.

### `reports/`
This folder contains the final deliverables of the penetration testing engagement:
- **pentest-report**: A comprehensive report summarizing findings, risks, and remediation advice.
- **findings-summary**: An executive summary for stakeholders.

### `scripts/`
Automation scripts used to conduct penetration testing and vulnerability scans.

### `juice-shop-setup.md`
A guide to set up the OWASP Juice Shop application locally for testing and training.

### `README.md`
Provides an overview of the project, instructions for setup, and how to use the resources in the repository.

## Notes
- **findings** is the primary folder for in-depth information on vulnerabilities, exploitation, and remediation.
- **reports** is where the final penetration testing report and summary of findings reside.
- **scripts** contains automation tools that streamline testing tasks.

This structure is designed to provide clear organization for efficient workflow and ease of access to important resources in the penetration testing process.


