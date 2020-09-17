#!/usr/bin/python3
"""
API
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    url = 'http://reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-agent': 'hama_chrab'}
    res = requests.get(url, headers=header,
                       params={'t': all, 'after': after})
    if not res or res.status_code == 400:
        return None
    for i in res.json().get('data')['children']:
        hot_list.append(i['data']['title'])
    after = res.json().get('data').get('after')
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
