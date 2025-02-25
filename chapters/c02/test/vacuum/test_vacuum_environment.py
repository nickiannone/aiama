import unittest
from chapters.c02.vacuum.reflex_vacuum_agent import ReflexVacuumAgent
from chapters.c02.vacuum.vacuum_environment import VacuumEnvironment
from chapters.c02.base.percept import Percept

class TestVacuumEnvironment(unittest.TestCase):
    def setUp(self):
        self.agent = ReflexVacuumAgent()
        self.environment = VacuumEnvironment([self.agent])

    def test_init(self):
        self.assertEqual(self.environment.state["location[A].status"], "Dirty")
        self.assertEqual(self.environment.state["location[B].status"], "Dirty")
        self.assertEqual(self.environment.state["agent[ReflexVacuumAgent].location"], "A")

    def test_get_percept(self):
        percept = self.environment.get_percept(self.agent)
        expected_percept = Percept("A", "Dirty")
        self.assertEqual(percept.info, expected_percept.info)

    def test_is_done(self):
        self.assertFalse(self.environment.is_done())
        self.environment.state["location[A].status"] = "Clean"
        self.environment.state["location[B].status"] = "Clean"
        self.assertTrue(self.environment.is_done())

if __name__ == '__main__':
    unittest.main()
