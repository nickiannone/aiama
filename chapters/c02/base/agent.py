from chapters.c02.base.action import Action
from chapters.c02.base.effect import Effect
from chapters.c02.base.environment import Environment
from chapters.c02.base.percept import Percept


class Agent:
    def __init__(self, name):
        self.name = name

    # Receive a Percept which can be matched to the appropriate Action
    def perceive(self, percept: Percept, environment: Environment) -> Action:
        raise NotImplementedError("This method should be overridden by subclasses")
    
    # React to the effects of the action performed by the acting agent
    def react(self, environment: Environment, acting_agent, action_effects: list[Effect]):
        pass