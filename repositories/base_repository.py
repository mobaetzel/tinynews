from typing import List, TypeVar, Generic, Type, Dict, Any

from pymongo.collection import Collection
from pymongo.database import Database

from models import BaseModel

T = TypeVar('T', bound=BaseModel)


class BaseRepository(Generic[T]):
    _collection: Collection = None

    def __init__(self, database: Database):
        self._collection = database.get_collection(self._get_collection_id())

    def _create(self, data: T) -> None:
        db_data = data.to_database()
        self._collection.insert_one(db_data)

    def _list(self, filter_dict=None) -> List[T]:
        results = self._collection.find(filter_dict)
        return [
            self._get_class(res)
            for res in results
        ]

    def _update(self, filter_dict, data) -> None:
        self._collection.update_one(filter_dict, {'$set': data})

    def _remove(self, filter_dict) -> None:
        self._collection.delete_many(filter_dict)

    def _get_collection_id(self) -> str:
        raise NotImplementedError

    def _get_class(self, data: Dict[str, Any]) -> T:
        raise NotImplementedError
