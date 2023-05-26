from logic.commandStates import CommandStates
from globals import *
from storage import load_data

persons = None
current_command_state = None

def init_model():
    global persons
    global current_command_state

    current_command_state = HOME
    persons = load_data()

def get_persons():
    global persons
    return persons

def get_persons_str():
    return (", ".join(map(str, persons)))

def set_persons(new_persons: dict):
    global persons
    persons = new_persons

def get_owe_summary():
    result = ""
    for person in persons:
        result += persons[person].owe_summary()

    return result

def get_pool_summary(persons):
    pool_data = {}
    for name in persons:
        pool_data[name] = 0
    for name in persons:
        pool_data[name] += persons[name].get_total_owings()
        for owee in persons:
            if owee != name:
                if persons[owee].get_owe_people()[name] > 0:
                    pool_data[name] -= persons[owee].get_owe_people()[name]
    return pool_data

def get_pool_summary_str(persons):
    pool_data = get_pool_summary(persons)

    result = "Pool Summary (+ve means owes pool, -ve means take from pool):\n\n"
    for name in pool_data:
        result += name + ": " + str(pool_data[name]) + "\n"

    return result



def set_current_command_state(command_state: CommandStates):
    global current_command_state
    current_command_state = command_state

def get_current_command_state():
    global current_command_state
    return current_command_state




