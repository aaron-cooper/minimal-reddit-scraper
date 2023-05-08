import requests
from Post import Post



url = r"https://reddit.com/r/ask_reddit/new.json"

r = requests.get(url, headers={'User-agent': 'acs-reddit-scraper'})

j = r.json()["data"]["children"]

def json_to_post(json):
    json = json["data"]
    return Post(json["title"], json["name"], json["created"], json["selftext"])

posts = list(map(json_to_post, j))

for title in map(lambda post: post.title, posts):
    print(title)


