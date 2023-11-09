#!/usr/bin/python3
"""Querries the reddit api based on a given subreddit"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/ajimoti)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        data = response.get("data")
        children = data.get("children")
        if children:
            for i in range(len(children)):
                print(children[i].get("data").get("title"))
    else:
        print("None")
