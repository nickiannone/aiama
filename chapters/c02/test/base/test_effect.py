import unittest
from datetime import datetime

from chapters.c02.base.effect import Effect

class TestEffect(unittest.TestCase):
    def setUp(self):
        self.agent = "test_agent"
        self.name = "test_name"
        self.key = "test_key"
        self.old_value = "old_value"
        self.new_value = "new_value"
        self.timestamp = datetime.now()

    def test_effect_initialization(self):
        effect = Effect(self.agent, self.name, self.key, self.new_value, self.old_value, self.timestamp)
        self.assertEqual(effect.agent, self.agent)
        self.assertEqual(effect.name, self.name)
        self.assertEqual(effect.key, self.key)
        self.assertEqual(effect.old_value, self.old_value)
        self.assertEqual(effect.new_value, self.new_value)
        self.assertEqual(effect.timestamp, self.timestamp)

    def test_effect_initialization_without_timestamp(self):
        effect = Effect(self.agent, self.name, self.key, self.new_value, self.old_value)
        self.assertEqual(effect.agent, self.agent)
        self.assertEqual(effect.name, self.name)
        self.assertEqual(effect.key, self.key)
        self.assertEqual(effect.old_value, self.old_value)
        self.assertEqual(effect.new_value, self.new_value)
        self.assertIsNotNone(effect.timestamp)

    def test_effect_repr(self):
        effect = Effect(self.agent, self.name, self.key, self.new_value, self.old_value, self.timestamp)
        expected_repr = f"Effect(name={self.name}, key={self.key}, old_value={self.old_value}, new_value={self.new_value}, timestamp={self.timestamp})"
        self.assertEqual(repr(effect), expected_repr)

    def test_get_state(self):
        effect = Effect(self.agent, self.name, self.key, self.new_value, self.old_value, self.timestamp)
        expected_state = {self.key: self.new_value}
        self.assertEqual(effect.get_state(), expected_state)
        # Apply the effect to a state dict
        applied_state = {}
        applied_state.update(effect.get_state())
        self.assertEqual(applied_state, expected_state)

    def test_revert_state(self):
        effect = Effect(self.agent, self.name, self.key, self.new_value, self.old_value, self.timestamp)
        expected_state = {self.key: self.old_value}
        self.assertEqual(effect.revert_state(), expected_state)
        # Apply the revert to a state dict
        reverted_state = {}
        reverted_state.update(effect.revert_state())
        self.assertEqual(reverted_state, expected_state)

if __name__ == '__main__':
    unittest.main()