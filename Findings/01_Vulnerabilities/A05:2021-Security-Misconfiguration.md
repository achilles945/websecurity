# A05:2021 - Security Misconfiguration

### Vulnerability 1: Weak or Unenforced Username Policy

- **Vulnerability**: Weak Username Policy for forgot-password page
- **Description**: The forgot-password page error handling problem. The application respond with security questions to valid usernames and does not respond to invalid username. This way attacker can Enumerate Usernames.
- **Severity**: Low
- **CWE-287**: CWE-204
- **Affected Components**: forgot-password page, Database Authentication System
- **Exploitability**: Easy – Any unauthenticated user can exploit this vulnerability.
- **Impact**: The attacker can Enumerate valid usernames to launch further attacks.
- **Proof-of-Concept**: Screenshot of Forgot password page responding to valid username
- **Remediation**: Ensure the application returns consistent generic error messages in response to invalid account name, password or other user credentials entered during the log in process.


### Vulnerability 2: Default Credentials

- **Vulnerability**: Default Credentials exist in for administrator
- **Description**:the default credentials ``admin@juice-sh.op:admin123`` are not replaced. attacker can log in as administrator with easily guessing these combinations 
- **Severity**: Medium to High
- **CWE**: CWE-512
- **Affected Components**: login page 
- **Exploitability**: Easy – Any unauthenticated user can exploit this vulnerability.
- **Impact**: Attacker can get Unauthorized access as administrator with high privileges.
- **Proof-of-Concept**: Screenshot of login page, Burpsuite Repeater
- **Remediation**: 
- Change Default Credentials
- Enforcing Strong Password Policies
- Implement Multi-Factor Authentication (MFA)


### Vulnerability 3: Detailed Error Messages 

- **Vulnerability**: Exposure of Detailed Error Messages (Security Misconfiguration)
- **Description**: The application reveals detailed error messages, including stack traces and internal file paths, to end users. This is a security misconfiguration where sensitive internal information is exposed, which could assist attackers in identifying potential vulnerabilities or misconfigurations within the application.
- **Severity**: Medium
- **CVEs**: Not applicable (since this is a configuration issue rather than a specific flaw tied to a known CVE).
- **Affected Components**: 
  - Application error handling
  - Express.js framework (or other used frameworks)
  - General server configuration
- **Exploitability**: Easy – This issue can be exploited by an attacker simply by triggering errors, which causes the application to leak stack trace information. Attackers can then use this information to map out the internal application structure or craft more sophisticated attacks.
- **Impact**: 
  - **Information Disclosure**: Sensitive details about the application’s internal workings, such as file paths and function names, are exposed.
  - **Potential for Further Exploitation**: Attackers may use the revealed information to launch targeted attacks, including identifying vulnerable endpoints, performing path traversal, or exploiting unprotected admin routes.
- **Proof-of-Concept**:  
  Example of the error message and stack trace that reveals sensitive internal paths and code locations:
    ```
    500 Error: Unexpected path: /rest/admin/configuration-file/
    
    at /juice-shop/build/routes/angular.js:38:18
    at Layer.handle [as handle_request] (/juice-shop/node_modules/express/lib/router/layer.js:95:5)
    at trim_prefix (/juice-shop/node_modules/express/lib/router/index.js:328:13)
    at /juice-shop/node_modules/express/lib/router/index.js:286:9
    at Function.process_params (/juice-shop/node_modules/express/lib/router/index.js:346:12)
    at next (/juice-shop/node_modules/express/lib/router/index.js:280:10)
    ...
    ```
- **Remediation**:
  1. **Disable Detailed Error Reporting in Production**: Ensure that detailed error messages (including stack traces and internal file paths) are not exposed in production environments. Configure the application to show generic error messages (e.g., `500 Internal Server Error`).
  2. **Use a Secure Error Handling Framework**: Implement a centralized error-handling middleware in frameworks like Express.js to catch and handle errors without exposing sensitive details.
  3. **Sanitize Logs**: Ensure that sensitive information such as file paths, user data, or stack traces is not logged in production. Use sanitized or obfuscated logs for auditing purposes.
  4. **Configure Application for Secure Error Handling**: Review the error-handling configuration in the app to ensure that only necessary details are logged, and the application responds with appropriate, non-sensitive error messages.


### Vulnerability: Exposure of PGP Public Key in `security.txt`

- **Vulnerability**: Information Exposure
- **Description**: The PGP public key is exposed in the `security.txt` file, which is intended to provide contact information and other details for security-related communication. While the public key itself is not inherently sensitive, its exposure in an unprotected file can provide attackers with information about the encryption infrastructure and potentially aid in cryptographic attacks if misused.
- **Severity**: Medium
- **CVEs**: None
- **Affected Components**: 
  - `security.txt` file
  - Cryptographic infrastructure (PGP key management)
- **Exploitability**: Low to moderate. An attacker with the public key could potentially attempt to send encrypted messages, but without access to the private key, this is not an immediate security risk.
- **Impact**: 
  - Exposure of cryptographic material that may aid attackers in social engineering or targeted attacks.
  - Potential misuse of the key if combined with other information.
  - Increased risk if the public key is used to secure sensitive communications, as attackers could analyze the key or try to find vulnerabilities in the encryption method.
- **Proof-of-Concept**: 
  - **File URL**: Accessing the `security.txt` file at `http://localhost:3000/.well-known/security.txt` reveals the PGP public key.
  - Example `security.txt` content:
    ```
    Contact: mailto:donotreply@owasp-juice.shop
    Encryption: https://keybase.io/bkimminich/pgp_keys.asc?fingerprint=19c01cb7157e4645e9e2c863062a85a8cbfbdcda
    ```
  - This URL provides access to the PGP public key used for encryption.
- **Remediation**:
  - Remove unnecessary or sensitive cryptographic information (like PGP public keys) from public files such as `security.txt`.
  - Ensure that public keys are shared securely and only through trusted channels if their exposure is not required.
  - Consider revising the purpose of the `security.txt` file to avoid disclosing excessive security-related information to the public.
  - If the PGP key must be publicly available, limit its exposure to the relevant parties and ensure that proper key management practices are followed.

### Vulnerability: Sensitive Directory Exposed via robots.txt

- **Vulnerability**: Sensitive Directory Exposure via `robots.txt`
- **Description**: The `robots.txt` file publicly exposes a sensitive directory (`/ftp/`) which contains confidential files. While `robots.txt` is used to guide web crawlers about which parts of a website to crawl, it is also publicly accessible. If the `/ftp/` directory is exposed via this file and remains publicly accessible, attackers can potentially exploit it to gain unauthorized access to confidential data.
- **Severity**: High
- **CVEs**: None (if this vulnerability is specific to a custom application setup, it may not have an existing CVE)
- **Affected Components**: 
  - `robots.txt` file
  - `/ftp/` directory (containing sensitive documents)
- **Exploitability**: Easy
  - Attackers can simply review the `robots.txt` file to identify sensitive directories and attempt to access them directly.
- **Impact**: 
  - Exposure of confidential files (e.g., sensitive documents, credentials, etc.)
  - Unauthorized access to critical data
  - Potential data breach or leakage of sensitive information
- **Proof-of-Concept**: 
  - `robots.txt` publicly lists `/ftp/`, allowing attackers to locate the folder.
  - `/ftp/` directory is accessible publicly, revealing confidential files.
  - Proof: A simple review of the `robots.txt` file followed by accessing the `/ftp/` directory via a browser or HTTP request reveals the sensitive files.
- **Remediation**:
  - **Restrict access** to sensitive directories (`/ftp/`) at the web server level. This can be done by using `.htaccess`, firewall rules, or appropriate server configurations to ensure that these directories are only accessible to authorized users.
  - **Do not use `robots.txt`** to protect sensitive data. It is not a security measure and can be easily bypassed by attackers.
  - Consider using **authentication and authorization** to secure sensitive folders.
  - Audit the contents of the `/ftp/` directory and ensure no sensitive files are publicly accessible.
  - **Remove references** to sensitive directories in the `robots.txt` file.
