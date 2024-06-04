#!/usr/bin/python3
"""
    Python script that fetch all title of the subreddit and do word count.
"""


def count_words(subreddit, word_list, word_count={}, after=None):
    """
        Prototype: count_word
        Args:
            subreddit:
            word_list:
            word_count:
            after: none
    """
    import requests

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()

    hot_post = [child.get("data").get("title")
            for child in data
            .get("data")
            .get("children")]
    if not hot_post:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in hot_post:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    if not data.get("data").get("after"):
        sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(word_count.items(),
                            key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, word_count,
                        data.get("data").get("after"))