

import datetime
from chapters.c02.base.action import Action
from chapters.c02.base.agent import Agent
from chapters.c02.base.effect import Effect
from chapters.c02.base.environment import Environment
from chapters.c02.base.percept import Percept


class ReflexVacuumAgent(Agent):
    def __init__(self):
        self.location = 'A'
        self.status = 'Dirty'

    def perceive(self, percept: Percept, environment: Environment) -> Action:
        # TODO: Verify we can unroll the percept tuple correctly!
        location, status = percept.info
        if status == 'Dirty':
            return ReflexVacuumAction('Suck')
        elif location == 'A':
            return ReflexVacuumAction('Right')
        else:
            return ReflexVacuumAction('Left')
        
class ReflexVacuumAction(Action):
    def __init__(self, name, cost=1):
        super().__init__(name, cost)
        self.name = name
        self.cost = cost

    def perform(self, agent: Agent, environment: Environment) -> list[Effect]:
        effects = []
        if self.name == 'Suck':
            old_status = environment.state.get(f'location[{agent.location}].status', 'Unknown')
            environment.clean(agent.location) # TODO: This should be a method of the environment!
            effects.append(Effect(agent, 'Clean', f'location[{agent.location}].status', 'Clean', old_status))
        elif self.name == 'Right':
            old_location = agent.location
            agent.location = 'B'
            effects.append(Effect(agent, 'Move', f'agent[{agent.name}].location', agent.location, old_location))
        elif self.name == 'Left':
            old_location = agent.location
            agent.location = 'A'
            effects.append(Effect(agent, 'Move', f'agent[{agent.name}].location', agent.location, old_location))
        return effects