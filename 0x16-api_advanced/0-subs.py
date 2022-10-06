#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers
for a given subreddit.
If an invalid subreddit is given, the function should return 0."""

from requests import get


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit

    Args:
        subreddit (str): subreddit to count subscribers
    """

    try:
        base_url = f'https://www.reddit.com/r/{subreddit}.json'
        request = get(base_url,
                      headers={
                          'user-agent': 'learn api by Careful_Reality8307'
                      })
        return request.\
            json()['data']['children'][0]['data']['subreddit_subscribers']
    except Exception:
        return 0
