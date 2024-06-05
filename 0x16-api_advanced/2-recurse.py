#!/usr/bin/python3

"""
a recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list of titles of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after
    )
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        after = response.json().get("data").get("after")
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
