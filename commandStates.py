from enum import Enum

class CommandStates(Enum):
    NEWBOOK = 'newBook'
    HOME = 'home'

    def __str__(self):
        return self.value