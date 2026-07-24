import datetime
import json
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://api.cloudflareclient.com/v0a2158/reg"

headers = {
    "User-Agent": "okhttp/3.12.1",
    "Content-Type": "application/json; charset=UTF-8",
    "Host": "api.cloudflareclient.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
}

body = {
    "install_id": "",
    "fcm_token": "",
    "tos": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    "model": "Android",
    "type": "Android",
    "locale": "en_US",
}

req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'), headers=headers)

try:
    with urllib.request.urlopen(req, context=ctx) as response:
        res = json.loads(response.read().decode('utf-8'))
        account_id = res["id"]
        token = res["token"]
        license_key = res["account"]["license"]
        
        print("\n" + "="*40)
        print("SUCCESS! YOUR WARP KEY IS:")
        print(license_key)
        print("="*40 + "\n")
except Exception as e:
    print(f"Error: {e}")
    with urllib.request.urlopen(req) as response:
        res_json = json.loads(response.read().decode("utf-8"))
        key = res_json.get("account", {}).get("license", "نامشخص")
        print("\n" + "=" * 40)
        print("SUCCESS! YOUR WARP+ KEY IS:")
        print(key)
        print("=" * 40 + "\n")
except Exception as e:
    print(f"Error executing API request: {e}")
    
