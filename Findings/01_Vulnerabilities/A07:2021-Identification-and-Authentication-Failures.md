# A07:2021 - Identification-and-Authentication-Failure

### Vulnerability 1: Username Enumeration

- **Vulnerability**: Username Enumeration via forgot-password page
- **Description**: The forgot-password page is vulnerable to a Username Enumeration attack. The application responds with security questions for valid usernames while providing no response for invalid usernames. This behavior allows an attacker to easily identify valid usernames by observing the application's responses.
- **Severity**: Low
- **CWE**: [CWE-287](https://cwe.mitre.org/data/definitions/287.html) - Improper Authentication
- **Affected Components**: 
  - Forgot-password page
  - Database Authentication System
- **Exploitability**: Easy – Any unauthenticated user can exploit this vulnerability by simply attempting to recover passwords for various usernames.
- **Impact**: The attacker can enumerate valid usernames, which can be leveraged for further attacks, such as targeted phishing or brute-force attacks on the login system.
- **Proof-of-Concept**: 
  - Screenshot of the forgot-password page showing a response for a valid username, indicating the presence of security questions.
- **Remediation**: 
  - Implement secure password recovery features that do not disclose whether an account exists. For example, provide a generic message such as "If this username exists, you will receive an email with instructions to reset your password."

---

### Vulnerability 2: Weak Lock Out Mechanism

- **Vulnerability**: No Lock Out Mechanism 
- **Description**: The login system lacks a proper lockout mechanism. After multiple failed login attempts, there is no account lockout or rate-limiting in place. This absence allows attackers to perform brute-force attacks, where they can attempt various username-password combinations without facing any restrictions.
- **Severity**: High (especially for applications handling sensitive data or admin privileges)
- **CWE**: 
  - [CWE-307](https://cwe.mitre.org/data/definitions/307.html) - Improper Restriction of Excessive Authentication Attempts
  - [CWE-287](https://cwe.mitre.org/data/definitions/287.html) - Improper Authentication
- **Affected Components**: 
  - Login page
  - Authentication System
  - User Database
- **Exploitability**: Easy to Moderate – Automated brute-force or credential stuffing attacks can be executed with minimal technical knowledge, making it accessible to a wide range of attackers.
- **Impact**: Attackers can gain unauthorized access to user accounts through brute-force attacks. If successful, this could lead to data theft, account compromise, privilege escalation, or unauthorized access to critical systems, potentially resulting in significant financial and reputational damage.
- **Proof-of-Concept**: 
  - Screenshots of successful brute-force attack attempts demonstrating the ability to bypass authentication due to the lack of lockout.
  - A Python script for a brute-force attack, illustrating the ease of executing such an attack without facing any restrictions.
- **Remediation**: 
  - Implement a time-based lockout mechanism that temporarily disables the account after a specified number of failed login attempts.
  - Introduce a self-service unlock feature that sends an email to the registered email address for account recovery.
  - Allow manual administrator unlock with positive user identification to ensure that only legitimate users can regain access to their accounts.
  - Consider implementing CAPTCHA or other forms of challenge-response tests after a certain number of failed attempts to further mitigate automated attacks.