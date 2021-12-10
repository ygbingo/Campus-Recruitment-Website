import requests
import json
import datetime

def get_all_xiaoice_jobs():
    """
    爬取岗位列表
    """
    url = "https://app.mokahr.com/api/outer/ats-jc-apply/website/jobs"
    headers = {
    'Content-Type': 'application/json'
    }

    payload = {
        "limit": 15,
        "needStat": True,
        "offset": 0,
        "orgId": "xiaobing",  # 可替换
        "site": "recommendation",  # 可替换
        "siteId": 26610  # 可替换
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    response = json.loads(response.text)
    jobs = response["data"]["jobs"]

    with open("jobs.json", "w") as f:
        json.dump(jobs, f, ensure_ascii=False)
        print("ok")

    return jobs

def get_job_detail(jobId):
    """
    爬取岗位细节
    """
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

def main(len=6):
    jobs = get_all_jobs()
    file = "jobs.md"
    f = open(file, "w+")
    f.write("# 投递模板 \n ### 邮箱 \n - 收件人: yanhuibin@xiaobing.ai \n - 主题：姓名-投递岗位-期望工作城市 \n - 内容：一句话介绍自己的优势 \n - 附件：个人简历.pdf \n")
    f.write("![image.png](https://pic.leetcode-cn.com/1624438530-VfRJKP-image.png)\n")

    for idx, job in enumerate(jobs):
        createT = job["createdAt"]
        jobId = job["id"]
        titile = "# " + job["title"]
        updatedAt = datetime.datetime.strptime(job["updatedAt"], "%Y-%m-%dT%H:%M:%S")
        print(updatedAt)
        jobDescribe = get_job_detail(jobId)
        jobDescribe = jobDescribe.replace("<br>", "\n").replace("</p>", "\n").replace("<p>", "").replace("&nbsp;", " ")
        
        f.write(str(updatedAt) + "\n" + titile + "\n" + jobDescribe + "\n")

        if idx > len:
            break
    
    
    f.close()
    

if __name__==main():
    lastUpdate = datetime.datetime.now()
    print(lastUpdate)

    main()