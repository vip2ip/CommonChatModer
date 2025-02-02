from aiogram import Dispatcher
from loguru import logger

from .chat_filters import IsGroup, IsPrivate
from .has_permissions import HasPermissions
from .is_reply import IsReplyFilter
from .user_filters import IsContributor


def setup(dp: Dispatcher):
    logger.info("Подключение filters...")
    text_messages = [
        dp.message_handlers,
        dp.edited_message_handlers,
        dp.channel_post_handlers,
        dp.edited_channel_post_handlers,
    ]

    dp.filters_factory.bind(HasPermissions, event_handlers=text_messages)
    dp.filters_factory.bind(IsReplyFilter, event_handlers=text_messages)
    dp.filters_factory.bind(IsContributor)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
