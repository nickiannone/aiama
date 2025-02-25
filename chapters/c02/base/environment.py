from chapters.c02.base.action import Action
from chapters.c02.base.agent import Agent
from chapters.c02.base.effect import Effect
from chapters.c02.base.percept import Percept


class Environment:
    def __init__(self, agents=None):
        self.state = {}
        self.agents = []
        if agents is not None:
            for agent in agents:
                self.add_agent(agent)

    # Return the current state of the environment as a percept for the agent
    # TODO: Environments should be able to return a percept that is specific to the agent, 
    # and this method should filter self.state to only provide what the agent is able to see!
    # This ensures that agents only perceive what they can observe in the environment.
    def get_percept(self, agent: Agent) -> Percept:
        # For now, we return the entire state as a percept.
        raise NotImplementedError("This method should be overridden by subclasses")

    # Determine if the environment has reached a terminal state.
    def is_done(self) -> bool:
        raise NotImplementedError("This method should be overridden by subclasses")
    
    # Add agent-specific state to the environment.
    def add_agent_state_to_environment(self, agent: Agent) -> None:
        pass

    # Applies the action to the environment and updates the state based on the action's effects.
    # It also notifies other agents of the action's effects.
    def apply_action(self, agent: Agent, action: Action) -> list[Effect]:
        # Apply the action to the environment to see what effects we make
        effects = action.perform(agent, self)

        # Update the state of the environment
        for effect in effects:
            self.state.update(effect.get_state())

        # Notify other agents of the effects of the action, letting them access the fully updated state indirectly
        for other_agent in self.agents:
            if other_agent != agent:
                other_agent.react(self, agent, effects)

        # Return the effects of the action
        return effects

    # Add an agent to the environment
    def add_agent(self, agent: Agent):
        self.agents.append(agent)
        self.add_agent_state_to_environment(agent)
