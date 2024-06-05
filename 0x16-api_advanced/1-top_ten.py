#!/usr/bin/python3

"""
a function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)
