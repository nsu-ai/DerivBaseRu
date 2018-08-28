import unittest

from src.Derivation import Derivation


class TestDerivation(unittest.TestCase):
    def setUp(self):
        self.derivation = Derivation()

    def tearDown(self):
        del self.derivation

    def test_rule977_01(self):
        """ Проверка правила 977. """
        results = self.derivation.derive(word_b='сильный', pos_b='adj', pos_a='adv')
        self.assertIn('сильно', results)


if __name__ == '__main__':
    unittest.main(verbosity=2)
