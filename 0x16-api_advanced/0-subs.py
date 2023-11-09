#!/usr/bin/python3
# queries the reddit api using a given subreddit
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for the given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/ajimoti)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        response = response.json()
        data = response.get("data")
        subscribers = data.get("subscribers")
        return subscribers
    return 0
