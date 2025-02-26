

from chapters.c02.base.agent import Agent
from chapters.c02.base.environment import Environment


class VacuumAgentRunner:
    def __init__(self, agents: list[Agent], environment: Environment):
        self.agents = agents
        self.environment = environment
        for agent in self.agents:
            self.environment.add_agent(agent)

    def run(self, steps):
        for _ in range(steps):
            for agent in self.agents:
                percept = self.environment.get_percept(agent)
                action = agent.perceive(percept)
                self.environment.apply_action(agent, action)
                print(f"Agent: {agent.name}, Percept: {percept}, Action: {action}")
            if self.environment.is_done():
                print("Environment is done.")
                break
        print("Simulation complete.")