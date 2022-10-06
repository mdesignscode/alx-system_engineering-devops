#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit
If not a valid subreddit, print None."""

from requests import get


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given subreddit

    Args:
        subreddit (str): the subreddit to be queried
    """

    try:
        base_url =\
            f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
        request = get(base_url,
                      headers={
                          'user-agent': 'learn api by Careful_Reality8307'
                      })
        if request.is_redirect:
            return
        [print(i['data']['title']) for i in request.json()['data']['children']]
    except Exception:
        print('None')
