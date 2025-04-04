# A05:2021 - Security Misconfiguration

# Vulnerability 1: Weak or Unenforced Username Policy

- **Vulnerability**: Weak Username Policy on the Forgot-Password Page
- **Description**: The forgot-password page in the application exhibits weak error handling behavior. When a user attempts to reset their password, the application returns specific responses based on whether the username is valid or not. If a valid username is provided, the application will prompt security questions or send a password reset link. However, if an invalid username is provided, the application remains silent or gives a generic error. This behavior allows attackers to easily enumerate usernames by trying different inputs and analyzing the response, potentially identifying valid usernames in the system.
- **Severity**: Low
- **CWE**: CWE-204 (Information Exposure Through Response to an Invalid Request)
- **Affected Components**:
  - Forgot-password page
  - Database authentication system
- **Exploitability**: Easy – Any unauthenticated user can exploit this vulnerability by trying different usernames on the forgot-password page and observing whether the application responds with a different message for valid usernames.
- **Impact**: 
  - **User Enumeration**: Attackers can enumerate valid usernames, which may allow them to target specific users with further attacks, such as brute-force password guessing, phishing attempts, or other social engineering attacks.
  - **Increased Risk of Account Compromise**: Once valid usernames are identified, attackers can then proceed with launching password guessing or brute-force attacks to gain unauthorized access to user accounts.
- **Proof-of-Concept**:
  - A screenshot can be provided showing the forgot-password page responding with security questions to a valid username, while the page remains silent or returns a generic error for invalid usernames.
- **Remediation**:
  - **Return Consistent Error Messages**: Ensure that the forgot-password page returns a generic, non-informative error message for both valid and invalid usernames. For example, use a message like "If the provided information is correct, you will receive instructions to reset your password."
  - **Obfuscate Account Existence**: Do not reveal whether the username is valid or invalid through the application's response. This makes it harder for attackers to enumerate usernames.
  - **Rate Limiting**: Implement rate-limiting or CAPTCHA challenges on the forgot-password page to mitigate brute-force enumeration attempts.
  - **Security Logging and Monitoring**: Track and monitor failed password reset attempts to detect and respond to potential attacks.

---

# Vulnerability 2: Default Credentials

- **Vulnerability**: Default Credentials for Administrator Account
- **Description**: The application is using default credentials for the administrator account (i.e., `admin@juice-sh.op:admin123`), which have not been changed. Default credentials are often well-known and easily guessable by attackers. In this case, the attacker can log into the application as an administrator with minimal effort, using common default username and password combinations. The presence of default credentials exposes the system to unauthorized access and further exploitation.
- **Severity**: Medium to High
- **CWE**: CWE-512 (Weak Password Recovery Mechanism)
- **Affected Components**:
  - Login page
  - Administrator account and authentication system
- **Exploitability**: Easy – Any unauthenticated user can attempt to log in using the default credentials, making this vulnerability trivial to exploit.
- **Impact**:
  - An attacker who successfully logs in with the default credentials can gain full administrative privileges.
  - If the attacker does not initially have administrative privileges
  - Once logged in as an administrator, the attacker can carry out malicious actions such as altering configurations, accessing sensitive data, or creating backdoors for further exploitation.
- **Proof-of-Concept**:
  - A screenshot of the login page showing the default credentials being used to successfully log in as an administrator, or a Burp Suite Repeater session demonstrating the login attempt with `admin@juice-sh.op:admin123` resulting in a successful login.
- **Remediation**:
  1. **Change Default Credentials Immediately**: Ensure that all default accounts, including the administrator account, have their default passwords changed to strong, unique credentials. 
  2. **Enforce Strong Password Policies**: Implement password policies that require strong, complex passwords for all users, especially for accounts with elevated privileges.
  3. **Implement Multi-Factor Authentication (MFA)**: Enforce the use of multi-factor authentication (MFA) for all administrative and privileged accounts.
  4. **Audit and Monitor Admin Accounts**: Regularly audit and monitor the usage of administrator accounts.
  5. **Disable or Remove Default Accounts**: If the application does not require the default administrator account, consider removing or disabling it entirely.


---

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

---

### Vulnerability 4: Exposure of PGP Public Key in `security.txt`

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

---

### Vulnerability 5: Sensitive Directory Exposed via robots.txt

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

---