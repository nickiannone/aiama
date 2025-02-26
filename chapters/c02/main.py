from chapters.c02.vacuum.reflex_vacuum_agent import ReflexVacuumAgent
from chapters.c02.vacuum.vacuum_agent_runner import VacuumAgentRunner
from chapters.c02.vacuum.vacuum_environment import VacuumEnvironment


def main():
    # Create an agent
    reflex_agent = ReflexVacuumAgent()

    # Create an environment
    env = VacuumEnvironment([reflex_agent])

    # Run the agents in the environment
    runner = VacuumAgentRunner([reflex_agent], env)

    # Print the results
    runner.run(10)
    print("Final Environment State:", env.state)
    print("Final Agent State:", reflex_agent.status)
    print("Simulation complete.")

if __name__ == "__main__":
    main()