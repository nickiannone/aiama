from chapters.c02.base.agent import Agent
from chapters.c02.base.effect import Effect
from chapters.c02.base.environment import Environment


class Action:
    def __init__(self, name, cost=1):
        self.name = name
        self.cost = cost

    def perform(self, agent: Agent, environment: Environment) -> list[Effect]:
        # TODO: Override this method in subclasses to define specific actions
        raise NotImplementedError("This method should be overridden by subclasses")

    def __repr__(self):
        return f"Action(name={self.name}, cost={self.cost})"