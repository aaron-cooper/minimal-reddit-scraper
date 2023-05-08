from Post import Post
from requests import Response

class ResponseToPosts:

    @staticmethod
    def json_to_post(json):
        json = json["data"]
        return Post(json["title"], json["name"], json["created"], json["selftext"])

    def convert(self, response: Response) -> Post:
        json = response.json()["data"]["children"]
        return list(map(ResponseToPosts.json_to_post, json))
