from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, я тут")

app = ApplicationBuilder().token("7698307866:AAGyAsVLM4h6jysuvDOMNnlq2nezHxIx7f0").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
