from person import Person
from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from model import get_persons, get_current_command_state
from globals import *
from storage import save_data

def init_message_handler():
    return MessageHandler(filters.TEXT & (~filters.COMMAND), parse_message)


def default_message_handler(message: str):
    return parse_transaction(message)

async def parse_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text

    print(str(get_current_command_state()))
    reply = command_state_functions.get(get_current_command_state(), default_message_handler)(message)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

def add_person(name: str):
    if (get_current_command_state() == NEWBOOK):
        new_person = Person(name)
        get_persons()[name] = new_person
        return "added " + new_person.name
    else:
        return "Error. Choose a command again."

def add_transaction(ower_str: str, owee_str: str, amount: float):
    persons = get_persons()

    if ower_str not in persons or owee_str not in persons:
        return "Invalid person entered"

    if ower_str == owee_str:
        return "Can't owe self"

    ower = persons[ower_str]
    owee = persons[owee_str]
    if owee.name not in ower.get_owe_people():
        ower.get_owe_people()[owee.name] = amount
    else:
        ower.get_owe_people()[owee.name] += amount

    save_data(get_persons())

    return "Transaction added:\n%s owes %s %s" % (ower, owee, amount)

def parse_transaction(message: str):
    tokens = message.split(" ")
    if len(tokens) != 3:
        return "Invalid transaction format. Format: <ower> <amount> <owee>"
    ower = tokens[0]
    amount = tokens[1]
    try:
        amount = float(amount)
    except:
        return "Invalid amount"
    owee = tokens[2]
    return add_transaction(ower, owee, float(amount))

command_state_functions = {
    HOME : default_message_handler,
    NEWBOOK : add_person
}