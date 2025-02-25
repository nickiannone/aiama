import unittest

from chapters.c02.base.action import Action


class TestAction(unittest.TestCase):
    def test_init(self):
        action = Action("TestAction", cost=5)
        self.assertEqual(action.name, "TestAction")
        self.assertEqual(action.cost, 5)
    
    def test_repr(self):
        action = Action("TestAction", cost=5)
        self.assertEqual(repr(action), "Action(name=TestAction, cost=5)")

    def test_perform_not_implemented(self):
        action = Action("TestAction")
        with self.assertRaises(NotImplementedError):
            action.perform(None, None)


if __name__ == '__main__':
    unittest.main()
