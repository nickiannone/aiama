

from chapters.c02.base.agent import Agent


class ReflexVacuumAgent(Agent):
    def __init__(self):
        self.location = 'A'
        self.status = 'Dirty'

    def program(self, percept):
        location, status = percept
        if status == 'Dirty':
            return 'Suck'
        elif location == 'A':
            return 'Right'
        else:
            return 'Left'