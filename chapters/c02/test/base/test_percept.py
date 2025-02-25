import unittest
from base.percept import Percept

class TestPercept(unittest.TestCase):
    def test_percept_initialization(self):
        p = Percept(1, 2, 3)
        self.assertEqual(p.info, (1, 2, 3))

    def test_percept_repr(self):
        p = Percept('a', 'b')
        self.assertEqual(repr(p), "Percept(info=('a', 'b'))")

    def test_percept_empty(self):
        p = Percept()
        self.assertEqual(p.info, ())

if __name__ == '__main__':
    unittest.main()