import requests
import time

url = "https://discord.com/api/webhooks/paste-your-webhook-here"
data = {
  "content": "@everyone L bozo malware, get a life",
  "embeds": None,
  "attachments": []
}

c = 0 # messages sent
d = 5 # delay
cd = 0 # since ratelimit

while True:
    s = requests.post(url=url, data=data).status_code
    if s == 429:
        d += 1
        print(f"Increasing delay to {d / 10} seconds to bypass ratelimits...")
        cd = 0

    else:
        c += 1
        cd += 1
        if cd > 4 and d > 0:
            d -= 1
            print(f"Decreasing delay to {d / 10} seconds to send faster...")

        print(f"Sent a message, have now sent a total of {c} messages (:<")

    time.sleep(d / 10) # to prevent ratelimits
