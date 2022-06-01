#!/usr/bin/python3
"""
function that returns the top ten posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ret top10 posts"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        posts = data['data']['children']
        for item in posts[:10]:
            print(item['data']['title'])
    else:
        print(None)
