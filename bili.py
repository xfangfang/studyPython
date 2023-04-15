import requests
import json
import time
import os
import sys

# 此脚本获得某条动态当前的点赞人
# 推荐定时运行

ACTIVITY_ID = 187760679912
REQUEST_TIME= int(time.time())
BASE = os.path.dirname(os.path.abspath(sys.argv[0]))
ALL_IN_ONE = f"{BASE}/bili_{ACTIVITY_ID}.json"
SPLIT_FILE = f"{BASE}/bili_{ACTIVITY_ID}_{REQUEST_TIME}.json"

def send_simple_message(title, msg):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox00000.mailgun.org/messages",
        auth=("api", "your api"),
        data={"from": "Helper <mailgun@sandbox00000.mailgun.org>",
            "to": ["your_email@qq.com"],
            "subject": f"bilibili error: {title}",
            "text": f"{msg}"})

def getLikeDetail(pn, ps):
    url = f"https://api.bilibili.com/x/msgfeed/like_detail?card_id={ACTIVITY_ID}&last_view_at=0&pn={pn}&ps={ps}&build=0&mobi_app=web"
    payload={}
    headers = {
      'Cookie': 'your bilibili cookie'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    j = response.json()
    if j['code'] != 0:
        print("send error msg")
        send_simple_message(ACTIVITY_ID, j['message'])
        return []
    return j['data']['items']


def getWholeData():
    data = []
    i = 1
    while True:
        p = getLikeDetail(i, 60)
        if len(p) == 0:
            return data
        data = data + p
        i += 1

def saveData():
    data = getWholeData()
    m = {}
    for i in data:
        mid = i['user']['mid']
        like = i['like_time']
        m[str(mid)] = like
    with open(SPLIT_FILE, "w") as f:
        json.dump(m, f)
    if not os.path.exists(ALL_IN_ONE):
        with open(ALL_IN_ONE, "w") as f:
            json.dump(m, f)
    return m

try:
    map_data = saveData()
except Exception as e:
    print("error1")
    send_simple_message("Undefined error 1", str(e))

try:
    with open(ALL_IN_ONE, "r") as f:
        old_map = json.load(f)
    for i in map_data:
        old_map[str(i)] = map_data[i]
    with open(ALL_IN_ONE, "w") as f:
        json.dump(old_map, f)
except Exception as e:
    print("error2")
    send_simple_message("Undefined error 2", str(e))