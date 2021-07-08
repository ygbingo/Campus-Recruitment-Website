import requests
import json

url = "https://app.mokahr.com/api/outer/ats-jc-apply/website/jobs"


headers = {
  'Content-Type': 'application/json'
}

payload = {
    "limit": 15,
    "needStat": True,
    "offset": 0,
    "orgId": "xiaobing",
    "site": "recommendation",
    "siteId": 26610
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

response = json.loads(response.text)
jobs = response["data"]["jobs"]

with open("jobs.json", "w") as f:
    json.dump(jobs, f, ensure_ascii=False)
    print("ok")

jobs = json.loads(jobs)