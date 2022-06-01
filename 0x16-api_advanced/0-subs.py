#!/usr/bin/python3
"""
function that returns the number of subscribers for a given subreddit
"""
import json
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ret subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
