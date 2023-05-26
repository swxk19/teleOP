import logging
import tokens
import json
from telegram.ext import ApplicationBuilder
from model import init_model
from logic.logic import init_logic

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(tokens.bot_token).build()
    init_model()
    init_logic(application)

    application.run_polling()


