import unittest
from simple_python_template import WordleMechanics

class TestTargetByGuess(unittest.TestCase):
    def test_guess(self):
        self.assertEqual("hello", "world")  # add assertion here


if __name__ == '__main__':
    unittest.main()
