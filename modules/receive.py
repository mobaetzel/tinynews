from telegram.ext import Updater, CommandHandler

from models import Subscription
from repositories import SubscriptionsRepository


def receive(token: str, subs_repo: SubscriptionsRepository) -> None:
    updater = Updater(
        token=token,
        use_context=True
    )
    dispatcher = updater.dispatcher

    def subscribe(update, context):
        chat_id = update.effective_chat.id
        url = update.message.text.replace('/subscribe', '').strip()

        sub = Subscription(chat_id, url)
        subs_repo.create(sub)

        context.bot.send_message(chat_id=update.effective_chat.id, text='Subscribed to {0}'.format(url))

    def unsubscribe(update, context):
        chat_id = update.effective_chat.id
        index = int(update.message.text.replace('/unsubscribe', '').strip())
        subscriptions = subs_repo.list(chat_id)
        subscription = subscriptions[index - 1]
        print(index, subscription, subscriptions)
        subs_repo.remove(subscription)
        context.bot.send_message(chat_id=update.effective_chat.id, text='Removed {0}'.format(subscription.url))

    def list_subs(update, context):
        chat_id = update.effective_chat.id
        subscriptions = subs_repo.list(chat_id)
        if len(subscriptions) == 0:
            context.bot.send_message(chat_id, text='You have currently no subscriptions')
        else:
            lines = []
            for index, sub in enumerate(subscriptions):
                lines.append(
                    '$' + str(index + 1) + ' ' + str(sub)
                )
            context.bot.send_message(
                chat_id,
                text='Subscriptions:\n\n{0}'.format('\n'.join(lines)),
            )

    subscribe_handler = CommandHandler('subscribe', subscribe)
    dispatcher.add_handler(subscribe_handler)

    unsubscribe_handler = CommandHandler('unsubscribe', unsubscribe)
    dispatcher.add_handler(unsubscribe_handler)

    list_handler = CommandHandler('list', list_subs)
    dispatcher.add_handler(list_handler)

    updater.start_polling()
    updater.idle()
