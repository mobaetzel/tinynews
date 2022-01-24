import sys

from pymongo import MongoClient
from pymongo.database import Database

from modules import send, receive
from repositories import SubscriptionsRepository
from services import token_service, mongo_service

token = token_service.get_token()

if token is None:
    print('Error no telegram bot token given')
    exit(1)

mongo_config = mongo_service.get_mongo_config()
if mongo_config is None:
    print('Error not all mongo config given')
    exit(1)

db_client: MongoClient = MongoClient('mongodb://{0}:{1}'.format(*mongo_config))
database: Database = db_client.get_database('tinynews')
subs_repo = SubscriptionsRepository(database)

command = sys.argv.pop()

if command == 'receive':
    receive(token, subs_repo)
elif command == 'send':
    send(token, subs_repo)
else:
    print('Unknown command {0}. Use either receive or send'.format(command))
    exit(1)
