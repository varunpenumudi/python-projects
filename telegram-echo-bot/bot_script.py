from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,MessageHandler, ContextTypes, filters
import time

import os
from dotenv import load_dotenv
load_dotenv()


# Command Handlers
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
        Command Handler for the /hello command
        replies with 'Hello {username}'
    """
    username = update.effective_user.first_name
    await update.message.reply_text(f'Hello {username}')


# Message Handlers
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
        Message Handler for the user
        replies with echo message i.e send same message the user sent
    """
    await update.message.reply_text(update.message.text)



if __name__ == "__main__":
    # Create the app object using token
    app = ApplicationBuilder().token(os.getenv("TOKEN")).build()

    # Add the created handlers to the app
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Poll/Run the app
    app.run_polling()
