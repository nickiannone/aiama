
from chapters.c02.base.agent import Agent
from chapters.c02.base.environment import Environment
from chapters.c02.base.percept import Percept
from chapters.c02.vacuum.vacuum_agent import VacuumAgent


class VacuumEnvironment(Environment):
    def __init__(self, agents: list[Agent]):
        super().__init__(agents)
        self.state["location[A].status"] = "Dirty"
        self.state["location[B].status"] = "Dirty"

    def clean(self, location: str) -> tuple[str, str]:
        old_status = self.state.get(f'location[{location}].status', 'Unknown')
        self.state[f'location[{location}].status'] = 'Clean'
        return 'Clean', old_status

    def add_agent_state_to_environment(self, agent: VacuumAgent) -> None:
        # Add agent-specific state to the environment
        self.state[f"agent[{agent.name}].location"] = agent.location

    def get_percept(self, agent: Agent) -> Percept:
        location = self.state[f"agent[{agent.name}].location"]
        status = self.state[f"location[{location}].status"]
        return Percept(location, status)
    
    def is_done(self):
        return self.state["location[A].status"] == "Clean" and self.state["location[B].status"] == "Clean"
