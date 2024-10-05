import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        
        self.calc = SimpleCalculator()

    def test_addition(self):
        
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_subtraction(self):
       
        self.assertEqual(self.calc.subtract(3, 1), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
    def test_multiplication(self):
        
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 1), 5)
    def test_division(self):
        try:
          self.assertEqual(self.calc.divide(4, 2), 2)

        except ZeroDivisionError:
              print("You can't divide by zero!")