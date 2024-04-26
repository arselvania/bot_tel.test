from telegram import Update, Updater, MessageHandler, filters

# Replace with your Telegram bot token
BOT_TOKEN = "6932522756:AAFR5X5NFCQU-PHrHclydWeimSw1jX3qVBY"

def start_handler(update: Update, context):
    """
    Handles the /start command.
    """
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id, "Hello!")

def main():
    """
    Starts the Telegram bot.
    """
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Add handler for the /start command
    dispatcher.add_handler(MessageHandler(Filters.command("start"), start_handler))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()