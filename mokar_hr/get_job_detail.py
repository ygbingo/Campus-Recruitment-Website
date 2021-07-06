import requests
import json

url = "https://app.mokahr.com/api/outer/ats-jc-apply/website/job"


headers = {
  'Content-Type': 'application/json',
  'Cookie': 'locale=en-US; moka-apply=YN7wXbPhqus5j1I%2F3NQrNuoVhPmv10M9e8GDgs3d0WabZ%2BbkOk7Nyvvipu5YhtEI; connect.sid=s%3AMaGA90k-V2uLwItBjSzK-8V-RafKZ5Ff.6nOS9DpbAxJ8VPh66euJ2nP%2FC7c5F%2BQBlCRktark904; acw_tc=2760827816255626305717587e99e7b415237232f297ace7aba12ea27d4fc5'
}

payload = {"orgId": "xiaobing", "jobId": "1c5950c8-e381-4f79-8e49-1e0f0fea0123", "siteId": 26610}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

response = json.loads(response.text)
jobDescript = response["data"]["jobDescription"]

print(jobDescript)