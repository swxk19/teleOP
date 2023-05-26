from person import Person
from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from logic import *
from globals import *

def init_message_handler():
    return MessageHandler(filters.TEXT & (~filters.COMMAND), parse_message)


def default_message_handler(message: str):
    return "test"

async def parse_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text

    print(str(get_current_command_state()))
    reply = command_state_functions.get(get_current_command_state(), default_message_handler)(message)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

def add_person(name: str):
    if (get_current_command_state() == NEWBOOK):
        new_person = Person(name)
        persons.append(new_person)
        return "added " + str(new_person)
    else:
        return "Error. Choose a command again."

def add_transaction(message: str):
    pass

command_state_functions = {
    HOME : add_transaction,
    NEWBOOK : add_person
}