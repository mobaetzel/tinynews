from telegram.utils.helpers import escape_markdown


class News:
    def __init__(self, title, link):
        self.title = title
        self.link = link

    def to_markdown(self):
        return '*{0}* [link]({1})'.format(
            escape_markdown(self.title, version=2),
            self.link
        )
