# A03:2021 - Injection


# Vulnerability 1: SQL Injection

- **Vulnerability**: SQL Injection in the login form.
- **Description**: The login form is vulnerable to SQL injection attacks. The user input is not properly sanitized or validated, allowing attackers to inject malicious SQL queries into the system. This flaw occurs when user input is directly embedded into SQL queries without proper handling, enabling an attacker to manipulate the query and bypass authentication mechanisms. In this case, an attacker could gain unauthorized access to the application or database by exploiting this vulnerability.
- **Severity**: High
- **OWASP Top 10**: A03:2021-Injection
- **CWE**: CWE-89 (Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection'))
- **WASC**: WASC-19 (Injection Flaws)
- **Affected Components**:
  - Login page
  - Database authentication system
- **Exploitability**: Easy – Any unauthenticated user can exploit this vulnerability by submitting a specially crafted SQL query through the login form.
- **Impact**:
  - **Bypass Authentication**: The attacker can bypass authentication and log into the application without valid credentials.
  - **Sensitive Data Exposure**: The attacker may gain access to sensitive user information such as usernames, passwords, or even administrative privileges.
  - **Privilege Escalation**: If the attacker can inject additional queries, they may escalate privileges and gain administrative control over the application or database.
  - **Data Corruption**: In extreme cases, SQL injection can lead to data manipulation or loss.

- **Proof-of-Concept**:
  - **Injection Payload**: 
    ```sql
    admin ' OR 1=1; -- 
    ```
  - **Explanation**: 
    - This SQL injection payload causes the SQL query to always return true (`OR 1=1`), which bypasses the authentication process. The `--` at the end is a comment in SQL, which disables the rest of the query (including the password check).
    - The resulting query could look like:
      ```sql
      SELECT * FROM users WHERE username = 'admin' OR 1=1; --' AND password = 'password';
      ```
      Since `1=1` is always true, the query will return the first user (or all users), and the attacker can bypass the login.

- **Remediation**:
  - **Use Parameterized Queries**: Always use parameterized queries or prepared statements. These methods separate SQL code from user data, ensuring that user input is treated as data and not executable code.
    - Example (PHP with PDO):
      ```php
      $stmt = $pdo->prepare('SELECT * FROM users WHERE username = :username AND password = :password');
      $stmt->execute(['username' => $username, 'password' => $password]);
      ```
  - **Validate and Sanitize Input**: Ensure that all user input is validated (e.g., checking for valid username formats) and sanitized (e.g., escaping special characters). Consider using a strict allowlist for acceptable characters in fields like usernames and passwords.
  - **Use ORM (Object-Relational Mapping)**: If possible, use an ORM to interact with the database. ORMs automatically handle input sanitization and help avoid raw SQL queries.
  - **Error Handling**: Avoid exposing detailed error messages to users, as they can provide valuable information to attackers. Instead, show generic error messages, such as "Invalid username or password."
  - **Database User Permissions**: Limit the privileges of the database user account that the application uses. Ensure it has only the necessary permissions for the application to function and avoid granting administrative access unless absolutely required.
  - **Regular Security Audits**: Perform regular security audits, including penetration testing and code reviews, to detect and remediate SQL injection vulnerabilities.

  ---

  ### Vulnerability 2: DOM-based Cross-Site Scripting (XSS) in Search Bar

- **Vulnerability**: DOM-based Cross-Site Scripting (XSS)
- **Description**: The search bar is vulnerable to DOM-based Cross-Site Scripting (XSS). This vulnerability occurs when the application fails to properly sanitize user input before rendering it in the DOM, allowing attackers to inject arbitrary JavaScript code. In this case, the attacker can inject malicious payloads like an `<iframe>` tag with external sources (such as SoundCloud), which is executed in the victim's browser when the malicious input is rendered. This can lead to session hijacking, stealing cookies, defacement, or other malicious actions.
- **Severity**: High
- **CWEs**: CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- **Affected Components**: 
  - Search bar functionality
  - Client-side JavaScript handling of user input
  - DOM manipulation without proper sanitization
- **Exploitability**: Easy
  - The attacker can inject malicious content like an `<iframe>` into the search bar. If the web application doesn't properly sanitize the input, the malicious content is embedded and executed in the user's browser when they interact with the search results.
- **Impact**:
  - An attacker can execute arbitrary JavaScript code, such as loading malicious content or hijacking the user's session.
  - This leads to the potential for stealing sensitive information (e.g., cookies, session tokens), defacing the site, redirecting users to malicious websites, or causing other unintended behavior in the user's browser.
  - The integrity of the user's session and personal information can be compromised.
- **Proof-of-Concept**: 
  - Inject the following payload into the search bar: 
    ```html
    <iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>
    ```
  - Upon submission of the search, the injected `<iframe>` will be rendered on the page, potentially executing the malicious content. In this example, the iframe loads an audio player from SoundCloud. However, an attacker can modify this to load malicious content or trigger more dangerous behavior.
  - A demonstration can be provided showing the injected iframe, which appears and behaves as intended, displaying external content that may be used for malicious purposes.
- **Remediation**:
  - **Sanitize user input**: All user-supplied data, especially input like search terms, should be properly sanitized before being used in the DOM.
  - **Use safe methods for DOM manipulation**: Avoid using methods like `innerHTML` to insert user data into the DOM. Instead, use `textContent`.
  - **Implement Content Security Policy (CSP)**: Implement a Content Security Policy (CSP)
  - **Conduct regular security testing**: Use security testing tools like OWASP ZAP, Burp Suite, or manual penetration testing to detect and mitigate DOM-based XSS vulnerabilities.
  - **Educate developers** on secure coding practices, particularly in handling user input and client-side scripting vulnerabilities.


---
