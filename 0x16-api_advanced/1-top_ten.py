#!/usr/bin/python3
"""Module for top_ten"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {
            'limit': 10
    }
    headers = {
            'user-agent': '0x16-api_advanced:\
v1 (by /u/markbonchi)'
    }
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 404:
        print("None")
        return
    res = r.json().get("data")
    [print(i.get("data").get("title")) for i in res.get("children")]
