# OWASP Top 10 - 2021

The **OWASP Top 10** represents the most critical security risks to web applications. It provides a foundational reference for understanding web security and testing web applications for common vulnerabilities. The list is periodically updated by the Open Web Application Security Project (OWASP) to reflect the evolving landscape of security risks.

## 1. **Broken Access Control**
   - **Description**: Access control is a fundamental security feature that ensures users can only access data and perform actions they are authorized to. When access control mechanisms are improperly implemented, attackers can gain unauthorized access to sensitive data or functions.
   - **Examples**:
     - Privilege escalation via parameter manipulation (e.g., changing user IDs in requests).
     - Direct access to unauthorized files or endpoints.
   - **Mitigation**:
     - Implement least privilege access controls.
     - Use secure authentication and authorization frameworks.
     - Apply proper role-based access control (RBAC).

## 2. **Cryptographic Failures**
   - **Description**: This refers to weaknesses in cryptographic protocols that lead to the exposure of sensitive data (e.g., passwords, credit card numbers) or vulnerabilities that make it easier for attackers to decrypt the data.
   - **Examples**:
     - Weak encryption algorithms (e.g., DES, RC4).
     - Insufficient key management.
     - Plaintext storage of sensitive information.
   - **Mitigation**:
     - Use modern, strong cryptographic algorithms (e.g., AES-256).
     - Ensure proper key management practices.
     - Use TLS (Transport Layer Security) for data transmission.

## 3. **Injection**
   - **Description**: Injection flaws, such as SQL, OS, and LDAP injection, occur when an attacker can send malicious input to a system, causing the application to execute unintended commands or queries.
   - **Examples**:
     - SQL Injection: Using SQL commands to manipulate a database.
     - Command Injection: Executing arbitrary commands on the operating system.
   - **Mitigation**:
     - Use prepared statements or parameterized queries.
     - Validate and sanitize all user inputs.
     - Implement least privilege for database accounts.

## 4. **Insecure Design**
   - **Description**: Insecure design vulnerabilities occur due to flaws in the architecture and design of an application. These vulnerabilities typically arise from insecure coding practices or poorly thought-out security controls in the design phase.
   - **Examples**:
     - Lack of secure design principles (e.g., not using secure coding standards).
     - Failure to implement secure default configurations.
   - **Mitigation**:
     - Incorporate secure design principles during development.
     - Conduct threat modeling early in the design phase.
     - Perform secure code reviews and static code analysis.

## 5. **Security Misconfiguration**
   - **Description**: Security misconfiguration refers to incorrectly or inadequately configured security settings that leave the application vulnerable. This could be a result of using default settings, exposing unnecessary features, or insecure file permissions.
   - **Examples**:
     - Unnecessary services running on the server.
     - Default credentials left unchanged.
     - Excessive permissions on sensitive files.
   - **Mitigation**:
     - Perform regular security audits and hardening.
     - Disable unnecessary features and services.
     - Use secure configurations and regularly update systems.

## 6. **Vulnerable and Outdated Components**
   - **Description**: Using outdated software components or libraries with known vulnerabilities can allow attackers to exploit those vulnerabilities. This includes the use of vulnerable third-party libraries and old versions of frameworks.
   - **Examples**:
     - Using outdated versions of Apache, OpenSSL, or other libraries with known vulnerabilities.
   - **Mitigation**:
     - Regularly update and patch software components.
     - Use tools to track and manage dependencies.
     - Remove unused or obsolete components.

## 7. **Identification and Authentication Failures**
   - **Description**: This category involves weaknesses in user authentication and session management. If attackers can compromise user credentials or session tokens, they can impersonate legitimate users.
   - **Examples**:
     - Weak password policies.
     - Insecure session management (e.g., predictable session tokens).
     - Insufficient multi-factor authentication.
   - **Mitigation**:
     - Implement strong password policies (e.g., minimum length, complexity).
     - Use multi-factor authentication (MFA) for sensitive actions.
     - Ensure secure session handling and timeouts.

## 8. **Software and Data Integrity Failures**
   - **Description**: This refers to failures in ensuring the integrity of software and data. Attackers can manipulate the integrity of data or software components if proper checks are not in place.
   - **Examples**:
     - Insecure deserialization allowing remote code execution.
     - Tampering with application code or data.
   - **Mitigation**:
     - Use digital signatures to verify data integrity.
     - Implement proper input validation and output encoding.
     - Avoid using insecure deserialization processes.

## 9. **Security Logging and Monitoring Failures**
   - **Description**: A lack of logging and monitoring can make it difficult to detect attacks or suspicious activities in a timely manner. Attackers can take advantage of this by executing attacks and remaining undetected.
   - **Examples**:
     - Failure to log security events (e.g., failed login attempts).
     - Lack of proactive monitoring for suspicious activity.
   - **Mitigation**:
     - Enable logging of all critical security-related events.
     - Implement intrusion detection systems (IDS) and security information and event management (SIEM) tools.
     - Regularly review logs for signs of malicious activity.

## 10. **Server-Side Request Forgery (SSRF)**
   - **Description**: SSRF vulnerabilities occur when a web application allows an attacker to send requests from the server to internal resources or services. This can lead to unauthorized access to internal systems or services.
   - **Examples**:
     - An attacker can send a request to internal services (e.g., a private API or database) by manipulating server-side request parameters.
   - **Mitigation**:
     - Validate and sanitize user inputs, especially URLs or IP addresses.
     - Implement strict access controls for internal services.
     - Use firewalls or network segmentation to limit the ability of attackers to reach internal systems.

---

## Additional Resources:

- [OWASP Top 10 2021 - Official Documentation](https://owasp.org/www-project-top-ten/)
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
