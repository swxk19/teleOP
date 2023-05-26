from person import Person
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from globals import *
from logic import get_current_command_state, set_current_command_state, persons

def init_command_handlers():
    handlers = []

    handlers.append(CommandHandler('state', state_command))

    handlers.append(CommandHandler('start', start_command))
    handlers.append(CommandHandler('newBook', new_book_command))
    handlers.append(CommandHandler('end', home_command))

    return handlers

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    set_current_command_state(HOME)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=":-)")

async def home_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    set_current_command_state(HOME)

    persons_string = "\n".join([str(person) for person in persons])
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Book contains:\n" + persons_string)

async def new_book_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    set_current_command_state(NEWBOOK)

    print (get_current_command_state())
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Who's going? Enter 1 name per message. Type '/end' to finish adding.")

async def state_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_command_state
    print(get_current_command_state())

    if get_current_command_state() == None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="None")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=str(get_current_command_state()))