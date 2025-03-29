# Information Gathering


## Conduct Search Engine Discovery Reconnaissance for Information Leakage

### Summary
    
    - Search engines can be used to perform reconnaissance on websites and web applications
    - There are direct and indirect elements to search engine discovery and reconnaissance
    - Direct
        - Relate to Searching the indexes and the associated content from caches
    - Indirect
        - Relate to learning sensitive design and configuration information by searching foumus, newgroups, and tendering websites

### Test Objective

    - Identify what sensitive design and configuration information of the application, system, or organization is exposed directly (on the organization’s website) or indirectly (via third-party services).

### How to Test

    Use a search engine to search for potentially sensitive information. This may include:

    - network diagrams and configurations;
    - archived posts and emails by administrators or other key staff;
    - logon procedures and username formats;
    - usernames, passwords, and private keys;
    - third-party, or cloud service configuration files;
    - revealing error message content; and
    - development, test, User Acceptance Testing (UAT), and staging versions of sites.

### Result
    



## Fingerprint Web Server

### Summary

    - Identifying the type and version of web server that a target is running on.
    - Often encapsulated in automated testing tools
    - Helps determine if application in vulnerable to attack

### Test Objectives

    - Determine the version and type of a running web server to enable further discovery of any known vulnerabilities.

### How to Test :

    - Techniques
        - Banner Grabbing
        - Eliciting Responses to malformed Rquest
        - Automated Tools

### Result

    -Banner Grabbing
        -HTTP/1.1 200 OK
        Accept-Ranges: bytes
        Access-Control-Allow-Origin: *
        Cache-Control: public, max-age=0
        Content-Type: text/html; charset=UTF-8
        Date: Fri, 28 Mar 2025 19:07:07 GMT
        Etag: W/"11708-195ddd992e0"
        Feature-Policy: payment 'self'
        Last-Modified: Fri, 28 Mar 2025 17:42:58 GMT
        Nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
        Report-To: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=%2FRix8MjtHqdoAhu9XT82NRSmDmhwkbYDJ1aqlnVebEE%3D\u0026sid=812dcc77-0bd0-43b1-a5f1-b25750382959\u0026ts=1743188827"}],"max_age":3600}
        Reporting-Endpoints: heroku-nel="https://nel.heroku.com/reports?s=%2FRix8MjtHqdoAhu9XT82NRSmDmhwkbYDJ1aqlnVebEE%3D&sid=812dcc77-0bd0-43b1-a5f1-b25750382959&ts=1743188827"
        Server: Heroku
        Vary: Accept-Encoding
        Via: 1.1 heroku-router
        X-Content-Type-Options: nosniff
        X-Frame-Options: SAMEORIGIN
        X-Recruiting: /#/jobs
        Connection: close
        Content-Length: 71432

    - Automated 
        - Nmap
        - Nikto
        - Netcraft





## Review Webserver Metafiles for Information Leakage

### Summary

    - Testing various metadata files for information leakage of web application's path(s), or functionality

### Test Objectives

    - Identify hidden or obfuscated paths and functionality through the analysis of metadata files.
    - Extract and map other information that could lead to better understanding of the systems at hand.


### How to Test

    - wget
    - curl
    - Dynamic Application Security Testing (DAST) tools
        - ZAP
        - Burp Suite
    - Google Dorks : inurl:

### Result




## Enumerate Application on Webserver




## Review Webpage Content for Information Leakage




## Identify Application Entry Points




## Map Execution Paths Through Application




## Fingerprint Web Application Framework




## Fingerprint Web Application




## Map Application Architecture





