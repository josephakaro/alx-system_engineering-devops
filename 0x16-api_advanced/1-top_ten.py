#!/usr/bin/python3
"""
    Python Script that fetches top ten subreddits through Reddit API url.
"""


def top_ten(subreddit):
    """
        Prototype: top_ten
        Args: subreddit
    """
    import requests
    limit = 9
    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit={}"
                            .format(subreddit, limit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
        for child in response.json().get("data").get("children")]