import requests

class Post:
    def __init__(self, title, name, time, text):
        self.title = title
        self.name = name
        self.time = time
        self.text = text



url = r"https://reddit.com/r/ask_reddit/new.json"

r = requests.get(url, headers={'User-agent': 'acs-reddit-scraper'})

j = r.json()["data"]["children"]

def json_to_post(json):
    json = json["data"]
    return Post(json["title"], json["name"], json["created"], json["selftext"])

posts = list(map(json_to_post, j))

for title in map(lambda post: post.title, posts):
    print(title)


