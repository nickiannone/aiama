import unittest
from chapters.c02.base.agent import Agent
from chapters.c02.base.percept import Percept
from chapters.c02.base.environment import Environment
from chapters.c02.base.action import Action
from chapters.c02.base.effect import Effect

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = Agent("TestAgent")
        self.environment = Environment([self.agent])

    def test_agent_initialization(self):
        self.assertEqual(self.agent.name, "TestAgent")

    def test_perceive_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.agent.perceive(Percept(), self.environment)

    def test_react(self):
        effect = Effect(agent=self.agent, name="TestEffect", key="location[A].status", new_value="Clean", old_value="Dirty")
        try:
            self.agent.react(self.environment, self.agent, [effect])
        except Exception as e:
            self.fail(f"react method raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()