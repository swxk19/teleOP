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
    name = name.lower()
    if (len(name.split(" ")) != 1):
        return "no spaces pls"

    if name == "all":
        return "don't b dum"

    if (get_current_command_state() == NEWBOOK):
        new_person = Person(name)
        get_persons()[name] = new_person
        return "added person: " + new_person.name
    else:
        return "Error. Choose a command again."

def add_transaction(ower_str: str, owee_str: str, amount: float):
    persons = get_persons()

    if (ower_str not in persons and ower_str != "all") or owee_str not in persons:
        return "Invalid person entered"

    if ower_str == owee_str:
        return "Can't owe self"

    if ower_str == "all":
        new_amount = amount / len(persons)
        for name in persons:
            if name != owee_str:
                add_transaction(name, owee_str, new_amount)

    else:
        ower = persons[ower_str]
        owee = persons[owee_str]

        difference = owee.get_owe_people()[ower.name] - amount
        if difference > 0:
            owee.get_owe_people()[ower.name] -= difference
        else:
            ower.get_owe_people()[owee.name] -= difference
            owee.get_owe_people()[ower.name] = 0

        save_data(get_persons())

    return "Transaction added:\n%s owes %s %s" % (ower_str, owee_str, amount)

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