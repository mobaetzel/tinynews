

class BaseModel:
    @staticmethod
    def from_database(database: dict) -> 'BaseModel':
        raise NotImplementedError

    def to_database(self) -> dict:
        raise NotImplementedError
