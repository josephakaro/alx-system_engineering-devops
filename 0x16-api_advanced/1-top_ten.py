#!/usr/bin/python3
"""
Python script that fetches the top ten
hot posts from a given subreddit through the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My-User-Agent"}
    params = {"limit": 10}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print("None")
        return
    
    try:
        data = response.json().get("data", {}).get("children", [])
    except ValueError:
        print("None")
        return
    
    if not data:
        print("None")
        return
    
    for post in data:
        title = post.get("data", {}).get("title", "None")
        print(title)