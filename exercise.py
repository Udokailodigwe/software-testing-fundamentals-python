# simple calculator test
import unittest


class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            # raise ArithmeticError("number cannot be divided by 0")
            return False
        return a // b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(10, 10)
        self.assertEqual(result, 20)

    def test_subtract(self):
        result = self.calculator.subtract(10, 10)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = self.calculator.multiply(10, 10)
        self.assertEqual(result, 100)

    def test_divide(self):
        result = self.calculator.divide(100, 10)
        self.assertEqual(result, 10)

    def test_incorrectDivision(self):
        result = self.calculator.divide(10, 0)
        self.assertFalse(result)
