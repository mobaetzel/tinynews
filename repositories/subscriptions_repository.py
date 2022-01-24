from typing import List, Dict, Any

from models import Subscription
from repositories.base_repository import BaseRepository


class SubscriptionsRepository(BaseRepository[Subscription]):
    def _get_collection_id(self) -> str:
        return 'subscriptions'

    def _get_class(self, data: Dict[str, Any]) -> Subscription:
        return Subscription.from_database(data)

    def create(self, sub: Subscription):
        return super()._create(sub)

    def all(self) -> List[Subscription]:
        return super()._list()

    def list(self, chat_id) -> List[Subscription]:
        return super()._list({
            'chat_id': chat_id,
        })

    def block(self, sub: Subscription) -> None:
        super()._update(
            sub.to_database(),
            {
                'blocked': True
            }
        )

    def remove(self, sub: Subscription) -> None:
        super()._remove(sub.to_database())
