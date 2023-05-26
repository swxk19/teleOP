from person import Person
from commandStates import CommandStates
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, Application
from globals import *

current_command_state = None
persons = []

def init_logic(application: Application):
    set_current_command_state(HOME)

def set_current_command_state(command_state: CommandStates):
    global current_command_state
    current_command_state = command_state

def get_current_command_state():
    global current_command_state
    return current_command_state





