import os
from typing import Union, Tuple


def get_mongo_config() -> Union[Tuple[str, str], None]:
    host = os.getenv('MONGO_HOST', None)
    port = os.getenv('MONGO_PORT', None)

    if host is None or port is None:
        return None
    return host, port
