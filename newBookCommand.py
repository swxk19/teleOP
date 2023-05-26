from person import Person
from commandStates import CommandStates
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, Application

async def new_book(current_command_state: CommandStates, context: ContextTypes.DEFAULT_TYPE):
    current_command_state = CommandStates.NEWBOOK

    await context.bot.send_message(chat_id=update.effective_chat.id, text="Who's going? Enter 1 name per message. Type '/doneAdding' to finish adding.")