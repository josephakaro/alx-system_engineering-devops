#!/usr/bin/python3
"""
    Fetch the Reddit API then returns
    the number of subscribers in for a subreddit.
    Example:
        Subreddit: 'Python'
        subscribers: '663773'
        ...
"""


def number_of_subscribers(subreddit):
    """\n
        Prototype: number_of_subscribers\n
        Arguments: subreddit\n
        Return: Number of Subscriber, 0 otherwise.\n

        Hint: Invalid subreddits may return a redirect to search results.
        Ensure that you are not following redirects.
    """
    import requests

    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
