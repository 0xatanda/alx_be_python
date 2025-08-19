import unittest
from simple_calculator import SimleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3, 1), 2)
        self.assertEqual(self.calc.subtract(-3, 4), -7)

    def test_multiply(self): 
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(4, 2), 8)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))

    def test_divide(self):
        self.assertEqual(self.calc.divide(20, 2), 10)