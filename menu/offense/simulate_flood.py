import requests
import time

# CONFIGURATION
# UPDATED: Port 5001 to match your dashboard
TARGET_URL = "http://localhost:5001/"
REQUEST_COUNT = 50  # Number of requests to send
DELAY_SECONDS = 0.1  # Very fast delay


def run_http_flood():
    print(f"[*] Starting HTTP Load Simulation (Flood) against {TARGET_URL}")
    print(f"[*] Sending {REQUEST_COUNT} requests...\n")

    success_count = 0
    fail_count = 0

    for i in range(REQUEST_COUNT):
        try:
            response = requests.get(TARGET_URL)
            if response.status_code == 200:
                success_count += 1
            else:
                fail_count += 1

            # Print a dot for progress
            print(".", end="", flush=True)

            time.sleep(DELAY_SECONDS)

        except Exception as e:
            fail_count += 1
            print("x", end="", flush=True)

    print("\n\n[*] Flood Simulation Summary:")
    print(f"    Total Requests: {REQUEST_COUNT}")
    print(f"    Successful (200 OK): {success_count}")
    print(f"    Failed/Other: {fail_count}")


if __name__ == "__main__":
    run_http_flood()