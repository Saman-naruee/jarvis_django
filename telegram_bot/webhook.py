from telegram.ext import Application
from django.conf import settings
from .handlers import setup_handlers
import logging

logger = logging.getLogger(__name__)

class TelegramBot:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
            setup_handlers(cls._instance)
        return cls._instance