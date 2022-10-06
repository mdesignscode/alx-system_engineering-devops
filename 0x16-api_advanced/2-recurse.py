#!/usr/bin/python3
"""returns a list containing the titles of all
hot articles for a given subreddit
If no results are found for the given subreddit,
the function should return None."""

from requests import get
from json import loads


def recurse(subreddit, hot_list=[], after=''):
    """returns a list containing the titles of all
    hot articles for a given subreddit

    Args:
        subreddit (str): the subreddit to be queried
        hot_list (list, optional): contains all hot articles. Defaults to [].
        after (str, optional): contains the next page
    """

    try:
        if after is not None:
            base_url = f'https://www.reddit.com/r/{subreddit}/hot.json?after='+after
            request = get(base_url,
                            headers={
                                'user-agent': 'learn api by Careful_Reality8307'
                            })

            if request.is_redirect:
                return

            for i in request.json()['data']['children']:
                hot_list.append(i['data']['title'])

            rd = loads(request.text)
            recurse(subreddit, hot_list=hot_list, after=rd['data']['after'])

        return hot_list

    except Exception:
        return None
