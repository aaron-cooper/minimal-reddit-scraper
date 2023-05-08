import requests
from Post import Post
from ResponseToPosts import ResponseToPosts

# _limits = [5, 10, 25, 50, 100]
_limits = [100]

class PostFetcher:
    def __init__(self, subreddit):
        self._url = rf"https://reddit.com/r/{subreddit}/new.json"
        self._posts = []
        self._prev_post = None
        self._which_limit = 0
        self._limit_strat = self._initial_limits
        self._converter = ResponseToPosts()
        self._curr = 0
        self._fetch = self._initial_fetch

    def _initial_fetch(self):
        url = self._url + f"?limit={self._limit_strat()}"
        response = requests.get(url, headers={'User-agent': 'acs-reddit-scraper'})
        self._posts = self._converter.convert(response)
        self._curr = 0
        self._fetch = self._subsequent_fetch


    def _subsequent_fetch(self):
        after_name = self._posts.pop().name
        url = self._url + f"?limit={self._limit_strat()}&after={after_name}"
        response = requests.get(url, headers={'User-agent': 'acs-reddit-scraper'})
        self._posts = self._converter.convert(response)
        self._curr = 0

    
    def next(self) -> Post:
        return self.__next__()
    
    def __next__(self):
        if self._curr == len(self._posts):
            self._fetch()
        self._curr += 1
        return self._posts[self._curr - 1]
    
    def __iter__(self):
        return self

    def _initial_limits(self):
        limit = _limits[self._which_limit]
        self._which_limit += 1
        if self._which_limit == len(_limits) - 1:
            self._limit_strat = self._subsequent_limits
        return limit

    def _subsequent_limits(self):
        return _limits[self._which_limit]