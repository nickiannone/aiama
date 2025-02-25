
from chapters.c02.base.agent import Agent


class VacuumAgent(Agent):
    def __init__(self, name):
        super().__init__(name)
        self.location = "A"
        self.status = "Dirty"
