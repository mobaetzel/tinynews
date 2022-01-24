from models.base_model import BaseModel
from typing import Dict, Any


class Subscription(BaseModel):
    def __init__(self, chat_id: str, url: str, blocked: bool = False):
        self.chat_id = chat_id
        self.url = url
        self.blocked = blocked

    @staticmethod
    def from_database(data: Dict[str, Any]) -> 'Subscription':
        return Subscription(
            data.get('chat_id', ''),
            data.get('url', ''),
            data.get('blocked', False),
        )

    def to_database(self) -> Dict[str, Any]:
        return {
            'chat_id': self.chat_id,
            'url': self.url,
            'blocked': self.blocked,
        }

    def __str__(self):
        return self.url + (
            ' (blocked)' if self.blocked else ''
        )
