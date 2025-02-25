from chapters.c02.base.effect import Effect

class Action:
    def __init__(self, name, cost=1):
        self.name = name
        self.cost = cost

    # TODO: Override this method in subclasses to define specific actions!
    def perform(self, agent, environment) -> list[Effect]:
        raise NotImplementedError("This method should be overridden by subclasses")

    def __repr__(self):
        return f"Action(name={self.name}, cost={self.cost})"