# TinyNews

TinyNews is a simple telegram bot for collecting and aggregating news via rss feeds.

## Prerequisites

Please make sure, that you have a bot ready for this project.
You can learn more about creating bots for telegram [here](https://core.telegram.org/bots#3-how-do-i-create-a-bot).

## Architecture

### Models

The models package contains all models for this project.
Models are either independent or based on the `BaseModel` which has stubs for serializing and deserializing the model for the database.

### Modules

The modules are the highest layer in this project.
They represent the two main jobs of this tool.
Receive messages from the clients and send them the aggregated news.

#### Receiver

This module loops infinitely and polls the telegram bot api.
Whenever a valid command was issued, a handler is called.
The bot can handle the following commands:

* `/subscribe <RSS-Link>`  
  Subscribes to a given RSS-Link
* `/unsubscribe <Subscription Id>`  
  Removes a subscription based on the given subscription id.
* `/list`  
  Lists all active subscriptions with their respective subscription ids.

#### Sender

The `send`-Module is used to iterate over all subscriptions and retrieve the subscribed feeds.
The retrieved data is than processed and reformatted and pushed via message to the subscribing user.

### Repositories

This package contains all repositories.
These classes represent a layer to handle data based on the business logic but encapsulate the underlying database technology.
This allows for an easier replacement of the underlying database.

### Services

This package contains stateless functionalities not strongly related to our business logic.

## Typing

This project uses mypy.
You can run `mypy --config-file mypy.ini .` to check the types.

## Env Variables

The configs for the database connection as well as the token for the telegram bot api are fetched from environment variables.
The following variables are utilized:

| Variable | Description |
| --- | --- |
| MONGO_HOST | The host address of the mongo database server |
| MONGO_PORT | The port of the mongo database server |
| TELEGRAM_TOKEN | The api token for the telegram bot |

## Docker

This project is dockerized.
You can use docker-compose to launch a working instance of the TinyNews-Bot.

Just insert you telegram bot api token in the `docker-compose.yml` and run `docker-compose up`.
The service is automatically launched and your bot is ready to go.

### Cron

The dockerfile uses a cronjob to run the send command every morning at 7:00 AM.
You can adjust this in the file `cronjob`.