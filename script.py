import datetime
import json
import random
import string
import ssl
import urllib.request
import urllib.error


def gen_str(length):
    return "".join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(length)
    )


def run():
    url = "https://api.cloudflareclient.com/v0a2158/reg"

    install_id = gen_str(22)
    fcm_token = f"{gen_str(22)}:APA91b{gen_str(134)}"

    body = {
        "install_id": install_id,
        "fcm_token": fcm_token,
        "tos": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%S.000Z"
        ),
        "model": "Android",
        "type": "Android",
        "locale": "en_US",
    }

    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "okhttp/3.12.1",
        "Host": "api.cloudflareclient.com",
    }

    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), headers=headers
    )

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            res = json.loads(response.read().decode("utf-8"))
            key = res.get("account", {}).get("license", "یافت نشد")
            print("\n" + "=" * 40)
            print("SUCCESS! YOUR WARP KEY IS:")
            print(key)
            print("=" * 40 + "\n")
    except urllib.error.HTTPError as e:
        print(f"\n[HTTP Error {e.code}]: {e.reason}")
        try:
            err_body = e.read().decode("utf-8")
            print(f"Cloudflare Response: {err_body}")
        except Exception:
            pass
    except Exception as e:
        print(f"\n[Error]: {e}")


if __name__ == "__main__":
    run()
