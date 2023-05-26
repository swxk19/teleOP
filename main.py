import logging
import tokens
import json
from person import Person
from commandStates import CommandStates
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

command_list = """
	/newBook
"""

async def parse_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_command_state

    message = update.message.text

    reply = command_state_functions.get(current_command_state)(message)
    print(reply)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)


def add_person(name: str):
    global current_command

    if (current_command_state == NEWBOOK):
        new_person = Person(name)
        persons.append(new_person)
        return "added " + str(new_person)
    else:
        return "Error. Choose a command again."

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_command_state
    current_command_state = START

    await context.bot.send_message(chat_id=update.effective_chat.id, text=":-)")

async def done_adding(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_command_state
    current_command_state = DONEADDING

    persons_string = "\n".join([str(person) for person in persons])
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Book contains:\n" + persons_string)
    print("ended global current state")

async def new_book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_command_state

    current_command_state = NEWBOOK

    await context.bot.send_message(chat_id=update.effective_chat.id, text="Who's going? Enter 1 name per message. Type '/doneAdding' to finish adding.")

async def state(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_command_state

    if current_command_state == None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="None")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=str(current_command_state))

current_command_state = None

if __name__ == '__main__':
    application = ApplicationBuilder().token(tokens.bot_token).build()
    persons = []

    START, NEWBOOK, DONEADDING = CommandStates

    command_state_functions = {
        NEWBOOK : add_person
    }


    state_handler = CommandHandler('state', state)

    start_handler = CommandHandler('start', start)
    new_book_handler = CommandHandler('newBook', new_book)
    done_adding_handler = CommandHandler('doneAdding', done_adding)

    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), parse_message)

    application.add_handler(state_handler)

    application.add_handler(start_handler)
    application.add_handler(new_book_handler)
    application.add_handler(done_adding_handler)

    application.add_handler(message_handler)

    application.run_polling()