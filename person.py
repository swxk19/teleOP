class Person:
    def __init__(self, name: str):
        self.name = name
        self.owe_people = {}

    def __str__(self):
        return self.name

    def owe_summary(self):
        result = self.name + "\n"
        for person in self.owe_people:
            result += "\t\towes " + person + " " + str(self.owe_people[person]) + "\n"
        return result

    def set_owe_people(self, people: dict):
        self.owe_people = people

    def get_owe_people(self):
        return self.owe_people

