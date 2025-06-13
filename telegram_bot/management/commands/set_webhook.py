from django.core.management.base import BaseCommand
from django.conf import settings
import ngrok
import asyncio
from telegram import Bot

class Command(BaseCommand):
    help = 'Set up Telegram webhook with ngrok'

    def handle(self, *args, **options):
        async def main():
            # Start ngrok tunnel
            listener = await ngrok.forward(8001)
            public_url = listener.url()
            self.stdout.write(f"ngrok tunnel: {public_url}")
            
            # Set webhook
            bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
            webhook_url = f"{public_url}/telegram/webhook/"
            await bot.set_webhook(webhook_url)
            self.stdout.write(f"Webhook set to: {webhook_url}")

        asyncio.run(main())