from chapters.c02.base.action import Action
from chapters.c02.base.agent import Agent
from chapters.c02.base.effect import Effect
from chapters.c02.base.environment import Environment
from chapters.c02.base.percept import Percept
from chapters.c02.vacuum.vacuum_agent import VacuumAgent
from chapters.c02.vacuum.vacuum_environment import VacuumEnvironment


class ReflexVacuumAgent(VacuumAgent):
    def __init__(self):
        super().__init__("ReflexVacuumAgent")

    def perceive(self, percept: Percept) -> Action:
        # Unpack the information from the percept
        # See VacuumEnvironment.get_percept() for the tuple structure
        self.location, self.status = percept.info
        if self.status == 'Dirty':
            return ReflexVacuumSuckAction()
        elif self.location == 'A':
            return ReflexVacuumMoveAction('Right')
        else:
            return ReflexVacuumMoveAction('Left')


class ReflexVacuumMoveAction(Action):
    def __init__(self, direction: str):
        super().__init__(direction, 1)
        self.direction = direction

    def perform(self, agent: VacuumAgent, environment: VacuumEnvironment) -> list[Effect]:
        old_location = agent.location
        if self.direction == 'Right':
            agent.location = 'B'
        else:
            agent.location = 'A'
        return [Effect(agent, 'Move', f'agent[{agent.name}].location', agent.location, old_location)]

class ReflexVacuumSuckAction(Action):
    def __init__(self):
        super().__init__('Suck', 1)

    def perform(self, agent: VacuumAgent, environment: VacuumEnvironment) -> list[Effect]:
        new_status, old_status = environment.clean(agent.location)
        return [Effect(agent, 'Clean', f'location[{agent.location}].status', new_status, old_status)]
