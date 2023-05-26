from enum import Enum

class CommandStates(Enum):
    START = 'start'
    NEWTRIP = 'newTrip'
    DONEADDING = 'doneAdding'

    def __str__(self):
        return self.value