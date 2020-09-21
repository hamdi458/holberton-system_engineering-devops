#!/usr/bin/python3
"""
API
"""
import json
import requests


def top_ten(subreddit):

    header = {'User-Agent': 'hamachrab'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(url, headers=header, allow_redirects=False,
                       params={"limit": 10}).json()
    try:
        for i in range(10):
            print(req["data"]["children"][i]["data"]["title"])
    except BaseException:
        print("None")
