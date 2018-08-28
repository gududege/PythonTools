from typing import Any, _KT, _VT


class MusicListItem(dict):

    def __init__(self, title: str, url: str, listid: str):

        self.title = title
        self.url = url
        self.listid = listid

    def __str__(self) -> str:
        return "{'title' : %s, 'url' : %s, 'listid' : %s}" % (self.title, self.url, self.listid)


