import requests

class Post:
    def __init__(self, title, name, time, text):
        self.title = title
        self.name = name
        self.time = time
        self.text = text