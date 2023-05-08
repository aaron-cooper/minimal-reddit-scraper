import requests
from Post import Post
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("subreddit", type=str)
arg_parser.add_argument("--past", "-p", default="1h")

args = arg_parser.parse_args()


url = rf"https://reddit.com/r/{args.subreddit}/new.json"

r = requests.get(url, headers={'User-agent': 'acs-reddit-scraper'})

j = r.json()["data"]["children"]

def json_to_post(json):
    json = json["data"]
    return Post(json["title"], json["name"], json["created"], json["selftext"])

posts = list(map(json_to_post, j))

for title in map(lambda post: post.title, posts):
    print(title)


