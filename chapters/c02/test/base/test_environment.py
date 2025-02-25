import unittest
from chapters.c02.base.environment import Environment
from chapters.c02.base.agent import Agent
from chapters.c02.base.action import Action
from chapters.c02.base.effect import Effect
from chapters.c02.base.percept import Percept

class TestEnvironment(unittest.TestCase):
    def setUp(self):
        self.agent = Agent()
        self.environment = Environment(agents=[self.agent])

    def test_initial_state(self):
        self.assertEqual(self.environment.state, {})
        self.assertIn(self.agent, self.environment.agents)

    def test_add_agent(self):
        new_agent = Agent()
        self.environment.add_agent(new_agent)
        self.assertIn(new_agent, self.environment.agents)

    def test_get_percept_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.environment.get_percept(self.agent)

    def test_is_done_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.environment.is_done()

    def test_apply_action(self):
        class MockAction(Action):
            def perform(self, agent, environment):
                return [MockEffect()]

        class MockEffect(Effect):
            def get_state(self):
                return {'key': 'value'}

        mock_action = MockAction()
        effects = self.environment.apply_action(self.agent, mock_action)
        self.assertEqual(self.environment.state, {'key': 'value'})
        self.assertEqual(len(effects), 1)
        self.assertIsInstance(effects[0], MockEffect)

if __name__ == '__main__':
    unittest.main()