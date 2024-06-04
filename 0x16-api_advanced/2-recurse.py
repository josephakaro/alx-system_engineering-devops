#!/usr/bin/python3
"""
    A python script that fetch top ten titles of a given subreddit
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
        Prototype: recurse
        Args:
            subreddit:
            hot_lists:
            count    :
            after    :
    """
    import requests

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 400:
        return None

    host_post = hot_list + [child.get("data").get("title")
                        for child in response.json()
                        .get("data")
                        .get("children")]

    data = response.json()
    if not data.get("data").get("after"):
        return host_post

    return recurse(subreddit, host_post, data.get("data").get("count"),
                data.get("data").get("after"))