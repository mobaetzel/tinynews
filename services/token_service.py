import os
from typing import Union


def get_token() -> Union[str, None]:
    return os.getenv('TELEGRAM_TOKEN', None)
