# A03:2021 - Injection


### Vulnerability 1: SQL Injection

- **Vulnerability**: SQL Injection in the login form.
- **Description**: The login form is vulnerable to SQL injection attacks. The user input is not properly sanitized, allowing attackers to inject malicious SQL queries.
- **Severity**: High
- **A03:2021-Injection**
- **CWE**: CWE-89
- **WASC**: WASC-19
- **Affected Components**: Login page, database authentication system.
- **Exploitability**: Easy – Any unauthenticated user can exploit this vulnerability.
- **Impact**: The attacker can bypass authentication and access sensitive user data, potentially gaining administrative privileges.
- **Proof-of-Concept**: Screenshot of the SQL injection payload used to bypass authentication.
- **Remediation**: 
  - Use parameterized queries or prepared statements to prevent SQL injection.
  - Validate and sanitize user input, especially for fields that interact with the database.