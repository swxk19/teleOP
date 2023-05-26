import logging
import tokens
import json
from person import Person
from commandStates import CommandStates
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, Application
from messageHandler import init_message_handler
from commandHandler import init_command_handlers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def init_handlers(application: Application):
    application.add_handler(init_message_handler())

    command_handlers = init_command_handlers()
    for command_handler in command_handlers:
        application.add_handler(command_handler)

if __name__ == '__main__':
    application = ApplicationBuilder().token(tokens.bot_token).build()
    init_handlers(application)


    application.run_polling()


