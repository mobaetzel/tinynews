from telegram import Bot

from repositories import SubscriptionsRepository
from services import feed_service


def send(token: str, subs_repo: SubscriptionsRepository) -> None:
    bot = Bot(token=token)
    subscriptions = subs_repo.all()

    for sub in subscriptions:
        if sub.blocked:
            continue
        feed_result = feed_service.load_feed(sub)
        if feed_result is None:
            subs_repo.block(sub)
            continue

        news = [news.to_markdown() for news in feed_result[:3]]
        bot.send_message(
            text='\n\n'.join(news),
            chat_id=sub.chat_id,
            parse_mode='MarkdownV2'
        )
