
# Table-driven agents use a set of percepts to determine behavior. 
# The agent's behavior is determined by a table that maps percept sequences to actions.
from chapters.c02.base.agent import Agent


class TableDrivenAgent(Agent):
    def __init__(self, table):
        self.table = table
        self.percept_sequence = []

    def act(self, environment, action):
        # Perform the action in the environment
        return environment.execute_action(action)

    def perceive(self, percept):
        self.percept_sequence.append(percept)
        action = self.table.get(tuple(self.percept_sequence), None)
        return action