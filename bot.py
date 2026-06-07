import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from deep_translator import GoogleTranslator

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    translated = GoogleTranslator(
        source='auto',
        target='en'
    ).translate(text)

    await update.message.reply_text(translated)

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        translate
    )
)

app.run_polling()
