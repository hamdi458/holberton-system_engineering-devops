#!/usr/bin/python3
"""
API
"""
import json
import requests


def number_of_subscribers(subreddit):

    header = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=header, allow_redirects=False).json()[
        "data"]["subscribers"]
    try:
        return (res)
    except BaseException:
        return(0)
