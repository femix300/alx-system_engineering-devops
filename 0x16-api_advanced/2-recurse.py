#!/usr/bin/python3
"""Querries the reddit api based on a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/ajimoti)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        data = response.get("data")
        after = data.get("after")
        count += data.get("dist")

        for results in data.get("children"):
            hot_list.append(results.get("data").get("title"))

        if after:
            return recurse(subreddit, hot_list, after, count)
        return hot_list

    else:
        return None
