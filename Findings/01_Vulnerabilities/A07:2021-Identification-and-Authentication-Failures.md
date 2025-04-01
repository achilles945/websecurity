# A07:2021 - Identification-and-Authentication-Failure

### Vulnerability 1: Username Enumeration

- **Vulnerability**: Username Enumeration via forgot-password page
- **Description**: The forgot-password page is vulnerable to Username Enumeration attack. The application respond with security questions to valid usernames and does not respond to invalid username. This way attacker can Enumerate Usernames.
- **Severity**: Low
- **CWE-287**: CWE-287
- **Affected Components**: forgot-password page, Database Authentication System
- **Exploitability**: Easy – Any unauthenticated user can exploit this vulnerability.
- **Impact**: The attacker can Enumerate valid usernames to launch further attacks.
- **Proof-of-Concept**: Screenshot of Forgot password page responding to valid username
- **Remediation**: 
- Implement secure password recovery features that do not reveal whether the account exists.


### Vulnerability 2: Weak Lock Out Mechanism

- **Vulnerability**: No Lock Out Mechanism 
- **Description**: The login system lacks a proper lockout mechanism. After multiple failed login attempts, there is no account lockout or rate-limiting. As a result, attackers can perform brute-force attacks, attempting various username-password combinations to gain unauthorized access.
- **Severity**: High (for applications with sensitive data or admin privileges)
- **CWE**: CWE-307, CWE-287
- **Affected Components**: Login page, Authentication System, User Database
- **Exploitability**:Easy to Moderate – Automated brute-force or credential stuffing attacks are simple to carry out with minimal knowledge.
- **Impact**:  Attackers can gain unauthorized access to user accounts by performing brute-force attacks. If successful, this could lead to data theft, account compromise, privilege escalation, or even unauthorized access to critical systems.
- **Proof-of-Concept**:Screenshots of successful brute-force attack attempts, Python script for brute force attack, showing the ability to bypass authentication due to the lack of lockout.
- **Remediation**:  
- Time Based lockout and unlock
- Self-service unlock (sends email to registered email address).
- Manual administrator unlock.
- Manual administrator unlock with positive user identification.

