from commandStates import CommandStates
from telegram.ext import  Application
from globals import *
from logic.messageHandler import init_message_handler
from logic.commandHandler import init_command_handlers

command_handlers = init_command_handlers()
message_handler = init_message_handler()

def init_logic(application: Application):
    mount_handlers(application)

def mount_handlers(application: Application):
    global message_handler
    global command_handlers

    application.add_handler(message_handler)

    for command_handler in command_handlers:
        application.add_handler(command_handler)