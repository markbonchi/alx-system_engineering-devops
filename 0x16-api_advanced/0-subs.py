#!/usr/bin/python3
"""Module for number_of_subscribers function"""


import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit."""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            'user-agent': '0x16-api_advanced:\
v1 (by /u/markbonchi)'
    }
    r = requests.get(url, header=headers).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
