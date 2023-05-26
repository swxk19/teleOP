from model import get_current_command_state, set_current_command_state, get_persons_str, get_persons, get_owe_summary, set_persons
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from globals import *
from storage import save_data

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
    persons = get_persons()

    for person in persons:
        for owee in persons:
            if person != owee:
                persons[person].get_owe_people()[owee] = 0

    save_data(get_persons())
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Book contains:\n" + get_persons_str())

async def new_book_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    set_persons({})
    set_current_command_state(NEWBOOK)

    await context.bot.send_message(chat_id=update.effective_chat.id, text="Who's going? Enter 1 name per message. Type '/end' to finish adding.")

async def state_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if get_current_command_state() == None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="None")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=get_owe_summary())