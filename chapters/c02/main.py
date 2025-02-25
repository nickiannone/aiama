from chapters.c02.vacuum.reflex_vacuum_agent import ReflexVacuumAgent
from chapters.c02.vacuum.table_driven_agent import TableDrivenAgent
from chapters.c02.vacuum.vacuum_agent_runner import VacuumAgentRunner
from chapters.c02.vacuum.vacuum_environment import VacuumEnvironment


def main():
    # Create an environment
    env = VacuumEnvironment()

    # Create a bunch of different agents
    table_driven_agent = TableDrivenAgent(env.action_table)
    reflex_agent = ReflexVacuumAgent()

    # Run the agents in the environment
    runner = VacuumAgentRunner(table_driven_agent, env)

    # Print the results

    # Visualize the results

if __name__ == "__main__":
    main()