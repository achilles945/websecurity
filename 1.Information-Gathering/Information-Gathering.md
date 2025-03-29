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
        HTTP/1.1 200 OK
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

### Summary

    - Identifying web application on a given infrastructure
    - The latter is usually specified as set of IP addresses, but may consist of a set of DNS symbolic names or a mix of the two

### Test Objectives

    - Enumerate the applications within scope that exist on a web server.

### How to Test

    - Assessment should idenify all the application accessible through given target
    - Internet Facing web servers
        - DNS and reverse-IP web-based search services and the use of search engines
    - Different Base URL
    - Non-standard Ports
    - Virtual Hosts

### Result
    - Non-standard URLs
        - https://juice-shop.herokuapp.com/#/
        - https://juice-shop.herokuapp.com/%23/
        - https://juice-shop.herokuapp.com/?ref=nullsweep.com#/
    
    - Non-standard Ports
        - nmap -Pn -sT -sV --top-port 10 juice-shop.herokuapp.com
            Nmap scan report for juice-shop.herokuapp.com (46.137.15.86)
            Host is up (0.14s latency).
            Other addresses for juice-shop.herokuapp.com (not scanned): 54.73.53.134 54.220.192.176
            rDNS record for 46.137.15.86: ec2-46-137-15-86.eu-west-1.compute.amazonaws.com

            PORT     STATE SERVICE        VERSION
            21/tcp   open  ftp?
            22/tcp   open  ssh?
            23/tcp   open  telnet?
            25/tcp   open  smtp?
            80/tcp   open  http           heroku-router
            110/tcp  open  pop3?
            139/tcp  open  netbios-ssn?
            443/tcp  open  ssl/https      heroku-router
            445/tcp  open  microsoft-ds?
            3389/tcp open  ms-wbt-server?
            2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
            ==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
            SF-Port80-TCP:V=7.94SVN%I=7%D=3/29%Time=67E7F22D%P=x86_64-pc-linux-gnu%r(G
            SF:etRequest,BF,"HTTP/1\.0\x20400\x20Bad\x20Request\r\nCache-Control:\x20n
            SF:o-cache,\x20no-store\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\
            SF:nDate:\x202025-03-29\x2007:44:25\.08047647\x20\+0000\x20UTC\r\nServer:\
            SF:x20heroku-router\r\nContent-Length:\x200\r\n\r\n")%r(HTTPOptions,C0,"HT
            SF:TP/1\.0\x20400\x20Bad\x20Request\r\nCache-Control:\x20no-cache,\x20no-s
            SF:tore\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nDate:\x202025-0
            SF:3-29\x2007:44:25\.509563838\x20\+0000\x20UTC\r\nServer:\x20heroku-route
            SF:r\r\nContent-Length:\x200\r\n\r\n")%r(FourOhFourRequest,BF,"HTTP/1\.0\x
            SF:20400\x20Bad\x20Request\r\nCache-Control:\x20no-cache,\x20no-store\r\nC
            SF:ontent-Type:\x20text/html;\x20charset=utf-8\r\nDate:\x202025-03-29\x200
            SF:7:44:36\.14991842\x20\+0000\x20UTC\r\nServer:\x20heroku-router\r\nConte
            SF:nt-Length:\x200\r\n\r\n");
            ==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
            SF-Port443-TCP:V=7.94SVN%T=SSL%I=7%D=3/29%Time=67E7F237%P=x86_64-pc-linux-
            SF:gnu%r(GetRequest,C0,"HTTP/1\.0\x20400\x20Bad\x20Request\r\nCache-Contro
            SF:l:\x20no-cache,\x20no-store\r\nContent-Type:\x20text/html;\x20charset=u
            SF:tf-8\r\nDate:\x202025-03-29\x2007:44:33\.264921586\x20\+0000\x20UTC\r\n
            SF:Server:\x20heroku-router\r\nContent-Length:\x200\r\n\r\n")%r(HTTPOption
            SF:s,C0,"HTTP/1\.0\x20400\x20Bad\x20Request\r\nCache-Control:\x20no-cache,
            SF:\x20no-store\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nDate:\x
            SF:202025-03-29\x2007:44:35\.936724375\x20\+0000\x20UTC\r\nServer:\x20hero
            SF:ku-router\r\nContent-Length:\x200\r\n\r\n")%r(FourOhFourRequest,C0,"HTT
            SF:P/1\.0\x20400\x20Bad\x20Request\r\nCache-Control:\x20no-cache,\x20no-st
            SF:ore\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nDate:\x202025-03
            SF:-29\x2007:44:38\.793607217\x20\+0000\x20UTC\r\nServer:\x20heroku-router
            SF:\r\nContent-Length:\x200\r\n\r\n");

            Read data files from: /usr/bin/../share/nmap
            Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
            Nmap done: 1 IP address (1 host up) scanned in 197.74 seconds

        - telnet




    - Virtual Hosts
        - nslookup
            nslookup juice-shop.herokuapp.com
                Server:		192.168.2.2
                Address:	192.168.2.2#53

                Non-authoritative answer:
                Name:	juice-shop.herokuapp.com
                Address: 54.73.53.134
                Name:	juice-shop.herokuapp.com
                Address: 54.220.192.176
                Name:	juice-shop.herokuapp.com
                Address: 46.137.15.86




## Review Webpage Content for Information Leakage

### Summary

    - Comments and metadata included into the HTML code might reveal internal information that should not be available to potential attackers
    - A review should be done in order to determine if any sensitive information leaked which could be used by attackers for abuse.

### Test Objectives

    - Review webpage comments and metadata to find any information leakage.
    - Gather JavaScript files and review the JS code to better understand the application and to find any information leakage.
    - Identify if source map files or other front-end debug files exist.


### How to Test

    - Review webpage comments and metadata
    - Identifying JavaScript Code and Gathering JavaScript Files
    - Identifying Source Map Files

### Result

    - Review webpage comments and metadata
    - Identifying JavaScript Code and Gathering JavaScript Files


    - Identifying Source Map Files


## Identify Application Entry Points

### Summary

    - Identify and map out areas within the application that should be investigated once enumeration and mapping have been completed

### Test Objectives

    - Identify possible entry and injection points through request and response analysis.

### How to Test

    - Requests


    - Responses

### Result


## Map Execution Paths Through Application




## Fingerprint Web Application Framework




## Fingerprint Web Application




## Map Application Architecture





