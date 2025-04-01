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