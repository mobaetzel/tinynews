from typing import List, Union

import requests
from bs4 import BeautifulSoup

from models import News, Subscription


def load_feed(sub: Subscription) -> Union[None, List[News]]:
    request = requests.get(sub.url)
    if request.status_code != 200:
        return None

    try:
        soup = BeautifulSoup(request.content, 'xml')
    except Exception as e:
        return None

    items = soup.find_all('item')

    return [
        News(
            node.find('title').string,
            node.find('link').string
        ) for node in items
    ]
