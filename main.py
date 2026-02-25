import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Hello! I am hosted on [TraxWizard](https://traxwizard.cloud).', parse_mode='Markdown')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Help message')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    # Create the application and pass your bot's token
    app = ApplicationBuilder().token("8543772090:AAGQl7zhDbZAdlXl-uy2Z_5NwqTbwA5qLnQ").build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot
    app.run_polling()

    #Telegram | @AccioTraxDinosaur
    #Instagram | @TraxDinosaur
    #Youtube | TraxDinosaur
    #Github | TraxDinosaur
    #https://traxdinosaur.github.io
    #https://traxdinosaur.github.io/APIs
    #https://traxdinosaurs.blog

if __name__ == '__main__':
    main()

