

from chapters.c02.base.agent import Agent
from chapters.c02.base.environment import Environment


class VacuumAgentRunner:
    def __init__(self, agent: Agent, environment: Environment):
        self.agent = agent
        self.environment = environment

    def run(self, steps):
        for _ in range(steps):
            percept = self.environment.get_percept(self.agent)
            action = self.agent.perceive(percept, self.environment)
            self.environment.apply_action(self.agent, action)
            print(f"Percept: {percept}, Action: {action}")
            if self.environment.is_done():
                break
        print("Simulation complete.")