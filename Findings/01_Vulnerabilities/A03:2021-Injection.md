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

  
  ### Vulnerability : DOM-based Cross-Site Scripting (XSS) in Search Bar

- **Vulnerability**: DOM-based Cross-Site Scripting (XSS)
- **Description**: The search bar in the OWASP Juice Shop web application is vulnerable to DOM-based Cross-Site Scripting (XSS). This vulnerability occurs when the application fails to properly sanitize user input before rendering it in the DOM, allowing attackers to inject arbitrary JavaScript code. In this case, the attacker can inject malicious payloads like an `<iframe>` tag with external sources (such as SoundCloud), which is executed in the victim's browser when the malicious input is rendered. This can lead to session hijacking, stealing cookies, defacement, or other malicious actions.
- **Severity**: High
- **CVEs**: None (Custom vulnerability, unlikely to have an existing CVE)
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
  - **Sanitize user input**: All user-supplied data, especially input like search terms, should be properly sanitized before being used in the DOM. Special characters such as `<`, `>`, `"`, and `'` should be encoded to prevent them from being interpreted as HTML or JavaScript.
  - **Use safe methods for DOM manipulation**: Avoid using methods like `innerHTML` to insert user data into the DOM. Instead, use `textContent` or safer DOM manipulation libraries to ensure input is treated as text and not executable code.
  - **Implement Content Security Policy (CSP)**: Implement a Content Security Policy (CSP) to restrict where scripts and content can be loaded from, minimizing the risk of executing untrusted or malicious JavaScript.
  - **Conduct regular security testing**: Use security testing tools like OWASP ZAP, Burp Suite, or manual penetration testing to detect and mitigate DOM-based XSS vulnerabilities.
  - **Educate developers** on secure coding practices, particularly in handling user input and client-side scripting vulnerabilities.
