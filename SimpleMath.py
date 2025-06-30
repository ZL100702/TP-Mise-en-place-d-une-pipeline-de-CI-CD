"""Module contenant des opérations mathématiques simples."""

class SimpleMath:
    """Classe avec des opérations arithmétiques de base."""

    @staticmethod
    def addition(a, b):
        """Additionne deux nombres."""
        return a + b
 test_simple_math.py
python
Copier
Modifier
import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(SimpleMath.addition(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
