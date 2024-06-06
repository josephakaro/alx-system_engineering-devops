#!/usr/bin/python3
"""
Python script that fetches all titles of a subreddit and performs a word count.
"""

import requests

def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Counts the occurrences of words in the titles of hot posts in a subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of words to count.
        word_count (dict): Dictionary to store the word counts.
        after (str): The id of the last post, used for pagination.
    """
    headers = {"User-Agent": "My-User-Agent"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return
    
    data = response.json()
    posts = data.get("data", {}).get("children", [])
    
    if not posts:
        return
    
    if not word_count:
        # Initialize word_count dictionary
        word_count = {word.lower(): 0 for word in word_list}
    
    for post in posts:
        title = post.get("data", {}).get("title", "")
        words = title.split()
        for word in words:
            cleaned_word = word.lower().strip(".,!?_")
            if cleaned_word in word_count:
                word_count[cleaned_word] += 1
    
    after = data.get("data", {}).get("after", None)
    if after:
        # Recursive call with the new 'after' value
        return count_words(subreddit, word_list, word_count, after)
    
    # If no more pages, sort and print the results
    if not after:
        sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
        for word, count in sorted_word_count:
            if count > 0:
                print(f"{word}: {count}")