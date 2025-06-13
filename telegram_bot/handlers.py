from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('👋 Hello! I am your Jarvis Assistant. How can I help you today?')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # For now, just echo the message
    await update.message.reply_text(f"You said: {text}")

def setup_handlers(application):
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))