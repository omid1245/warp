import datetime
import json
import random
import string
import urllib.request


def gen_str(length):
    return "".join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(length)
    )


url = "https://api.cloudflareclient.com/v0a1925/reg"

body = {
    "install_id": gen_str(22),
    "fcm_token": f"{gen_str(22)}:APA91b{gen_str(134)}",
    "tos": datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%S.000Z"
    ),
    "model": "Android",
    "type": "Android",
    "locale": "en_US",
}

data = json.dumps(body).encode("utf-8")
headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "okhttp/3.12.1",
}

req = urllib.request.Request(url, data=data, headers=headers)

try:
    with urllib.request.urlopen(req) as response:
        res_json = json.loads(response.read().decode("utf-8"))
        key = res_json.get("account", {}).get("license", "نامشخص")
        print("\n" + "=" * 40)
        print("SUCCESS! YOUR WARP+ KEY IS:")
        print(key)
        print("=" * 40 + "\n")
except Exception as e:
    print(f"Error executing API request: {e}")
    
