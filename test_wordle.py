import unittest
from simple_python_template import WordleMechanics

class TestTargetByGuess(unittest.TestCase):
    def test_guess(self):
        self.target_word = "hello"
        self.guess = "world"
        self.WordleMechanics(self.target_word, self.guess)
        self.assertEqual(WordleMechanics())


if __name__ == '__main__':
    unittest.main()
