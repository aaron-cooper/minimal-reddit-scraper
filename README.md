# Minimal Reddit Scraper

Script to download a lightweight version of the most recent posts of a subreddit.

## Using

### Install dependencies:
```
pip install -r requirements.txt
```

### Run `scrape.py`:
```
python scrape.py subreddit [--age AGE]
```
`AGE` specifies the maximum age of the posts which should be printed. It should be formatted like `NdNhNmNs`
where `N` is a non-negative integer. Only one unit of time is required, so `30d` or `5m` are both valid.
The default is 1 hour.

`subreddit` should be the name of a subreddit as it appears in a reddit URL. For example, to download
posts from `r/c_programming`, `subreddit` would be `c_programming`.

## `PostFetcher`
A class for getting posts from a subreddit and converting them to `Post` objects. A `PostFetcher` can be treated
as an iterable/iterator, or you can call the `next` method. `PostFetcher` provides posts as `Post` objects
in reverse chronological order of when they were posted. `scrape.py` is basically just an example of how to use
it, it'd be more useful to use this class directly in your own script.

## `Post`
### `title`
The title of a reddit post
### `name`
A posts "fullname"  recognized by the Reddit API.
### `time`
Unix time of when a post was posted.
### `text`
The text of a the post. More specifically it's the contents of the `selftext` property from the Reddit API.