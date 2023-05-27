from logic.commandStates import CommandStates

NEWBOOK, HOME = CommandStates

command_list = """
	/newBook
"""

data_file_name = "data.json"

HELP_TEXT = """Commands:\n
/start: :-)
/newBook: deletes everything and adds new people
/end: finish adding people
/log: view specifically what each person owes
/pool: view summary of what each person contributes to pool"""