# A01:2021 - Broken Access Control

### Vulnerability 1: Unauthorized Access 

- **Vulnerability**: Unauthorized Access to application-configuration.js
- **Description**: The application exposes sensitive administrative endpoints (`/rest/admin/application-configuration` and `/rest/admin/application-version`) to unauthenticated users, allowing them to retrieve application version and configuration details. This violates access control principles and can lead to information leakage.
- **Severity**: High
- **CWEs**: N/A
- **Affected Components**: 
  - `/rest/admin/application-configuration`
  - `/rest/admin/application-version`
- **Exploitability**: Easy
- **Impact**: 
  - Information disclosure: Attackers can obtain sensitive data such as the application version and configuration, which could be used to exploit known vulnerabilities.
  - Privilege escalation: If an attacker gains knowledge of the admin interface or other configurations, they could attempt to escalate their privileges or perform unauthorized actions.
  - Remote Code Execution (RCE): The disclosed application version or configuration could be used to exploit vulnerabilities in the system.
- **Proof-of-Concept**: 
  - As an unauthenticated user, accessing the endpoints `http://localhost:3000/rest/admin/application-configuration` and `http://localhost:3000/rest/admin/application-version` reveals sensitive application data (e.g., `{"version":"17.2.0"}`). 
  - The existence of these endpoints without proper authentication allows attackers to gain information that should be protected.
- **Remediation**: 
  - Implement proper authentication and authorization checks for all administrative endpoints.
  - Ensure that sensitive endpoints like `/rest/admin/application-configuration` and `/rest/admin/application-version` are only accessible to authenticated users with appropriate administrative roles.
  - Apply the principle of least privilege, ensuring that only authorized users can access configuration and versioning details.
  - Review and secure all endpoints in the `/admin` directory to prevent unauthorized access.


### Vulnerability: Broken Access Control - Sensitive Directory Exposure via `/ftp/`

- **Vulnerability**: Sensitive Directory Exposure via `/ftp/` Directory
- **Description**: The `/ftp/` directory is publicly accessible without proper access controls, despite containing potentially sensitive or confidential files. This exposure can lead to unauthorized access to files and data, increasing the risk of data breaches, information leaks, and potential exploitation.
- **Severity**: High
- **CVEs**: None (Custom vulnerability, unlikely to have an existing CVE)
- **Affected Components**: 
  - `/ftp/` directory (containing sensitive documents or data)
  - Web server configuration allowing access to `/ftp/` directory
- **Exploitability**: Easy
  - Attackers can directly access the `/ftp/` directory by browsing the website or attempting to access known paths. If directory listing is enabled, attackers may be able to view all files within the directory.
- **Impact**:
  - Unauthorized access to sensitive documents, internal data, or configuration files.
  - Risk of data leakage or data breach.
  - Potential for attackers to manipulate, delete, or steal sensitive information.
- **Proof-of-Concept**: 
  - Public access to the `/ftp/` directory can be confirmed by browsing to the directory path, e.g., `http://example.com/ftp/`, where sensitive files are accessible without authentication.
  - Screenshot showing accessible files within `/ftp/` directory, which should be restricted.
- **Remediation**:
  - **Restrict access** to the `/ftp/` directory via server-level configurations (e.g., using `.htaccess` or firewall rules to limit access to authorized users only).
  - **Remove directory listing** for the `/ftp/` directory to prevent attackers from viewing the contents of the folder.
  - **Implement authentication and authorization** mechanisms for accessing sensitive directories, ensuring that only legitimate users can access the data.
  - **Encrypt sensitive files** within the `/ftp/` directory to prevent unauthorized access even if the files are exposed.
  - **Audit and remove sensitive files** from publicly accessible directories. Ensure that sensitive data is not left in directories that are accessible without proper controls.


### Vulnerability : Unauthorized Feedback Submission via User ID Manipulation

- **Vulnerability**: Broken Access Control (Insecure Direct Object Reference - IDOR)
- **Description**: The application allows users to manipulate the `userID` parameter in the request, enabling them to impersonate another user and submit feedback on their behalf. This issue arises from insufficient authorization checks, allowing unauthorized actions.
- **Severity**: High
- **CVEs**: None (Custom vulnerability, unlikely to have an existing CVE)
- **Affected Components**: 
  - Feedback submission functionality
  - User authentication and authorization mechanisms
- **Exploitability**: Easy
  - The attacker can use browser developer tools (e.g., "Inspect Element" or "Network" tab) to change the `userID` parameter in the request to impersonate another user and submit feedback.
- **Impact**:
  - Users can perform actions that they are not authorized to perform, such as submitting feedback as other users, which could lead to false data, impersonation, and potential data integrity issues.
  - There is a risk of malicious input or harmful content being submitted in feedback on behalf of other users.
- **Proof-of-Concept**: 
  - Using browser developer tools, inspect the request containing the `userID` parameter.
  - Modify the `userID` value to that of another user and submit the feedback, which will be accepted as if it was submitted by the impersonated user.
  - Screenshot of the modified `userID` value in the request and successful feedback submission from the impersonated user.
- **Remediation**:
  - **Implement proper access control**: Ensure that users can only perform actions on data and resources they are authorized to access, including feedback submission.
  - **Perform validation and authorization checks**: Check that the user performing actions (e.g., submitting feedback) is the same as the user linked to the data being manipulated (e.g., `userID`).
  - **Avoid exposing sensitive identifiers** like `userID` in URLs or parameters. If necessary, encrypt or obfuscate these identifiers to prevent tampering.
  - **Test for and prevent Insecure Direct Object References (IDOR)** by performing thorough security testing and validating that each user can only access and modify their own data.
  - **Audit and log** all user interactions with sensitive actions, like feedback submission, to detect potential abuse or attacks.
