class Post:
    def __init__(self, title, name, time, text):
        self.title = title
        self.name = name
        self.time = time
        self.text = text

    def __str__(self) -> str:
        return f'Post({repr(self.title)}, {repr(self.name)}, {repr(self.time)}, {repr(self.text)})'