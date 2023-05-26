from person import Person
from commandStates import CommandStates
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, Application
from globals import *

persons = None
current_command_state = None

def init_model():
    global persons
    global current_command_state

    current_command_state = HOME
    persons = {}

def get_persons():
    global persons
    return persons

def get_persons_str():
    return (", ".join(map(str, persons)))

def get_owe_summary():
    result = ""
    for person in persons:
        result += persons[person].owe_summary()

    return result

def set_current_command_state(command_state: CommandStates):
    global current_command_state
    current_command_state = command_state

def get_current_command_state():
    global current_command_state
    return current_command_state




