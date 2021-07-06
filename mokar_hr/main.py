import requests
import json

def get_all_jobs():
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

    print(jobs)

def get_job_detail(jobId):
    url = "https://app.mokahr.com/api/outer/ats-jc-apply/website/job"
    headers = {
    'Content-Type': 'application/json',
    }
    payload = {"orgId": "xiaobing", "jobId": jobId, "siteId": 26610}

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    response = json.loads(response.text)
    jobDescript = response["data"]["jobDescription"]
    print(jobDescript)
    return jobDescript