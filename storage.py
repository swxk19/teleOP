import json
from globals import data_file_name
from person import Person

def serialize_person(person):
    return {"name": person.name, "owees": person.owe_people}

def save_data(persons):
    data = []
    for name in persons:
        person = persons[name]
        data.append(serialize_person(person))

    json_data = json.dumps(data, indent=4, sort_keys=True)
    filename = data_file_name

    with open(filename, "w") as file:
        file.write(json_data)

def load_person(obj):
    person = Person(obj["name"])
    person.set_owe_people(obj["owees"])
    return person

def load_data():
    with open(data_file_name, "r") as file:
        json_data = json.load(file)

    persons = []
    for obj in json_data:
        person = load_person(obj)
        persons.append(person)

    loaded_person_dict = {}
    for person in persons:
        loaded_person_dict[person.name] = person

    return loaded_person_dict

