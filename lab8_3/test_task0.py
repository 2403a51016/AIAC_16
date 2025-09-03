import unittest
from task0 import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator(10, 5, "add"), 15)
        self.assertEqual(calculator(-3, 7, "add"), 4)
        self.assertEqual(calculator(0, 0, "add"), 0)

    def test_subtraction(self):
        self.assertEqual(calculator(10, 5, "subtract"), 5)
        self.assertEqual(calculator(5, 10, "subtract"), -5)
        self.assertEqual(calculator(0, 0, "subtract"), 0)

    def test_multiplication(self):
        self.assertEqual(calculator(10, 5, "multiply"), 50)
        self.assertEqual(calculator(-2, 3, "multiply"), -6)
        self.assertEqual(calculator(0, 100, "multiply"), 0)

    def test_division(self):
        self.assertEqual(calculator(10, 5, "divide"), 2)
        self.assertEqual(calculator(9, 2, "divide"), 4.5)
        self.assertEqual(calculator(0, 5, "divide"), 0)

    def test_division_by_zero(self):
        self.assertEqual(calculator(10, 0, "divide"), "Error: Division by zero")
        self.assertEqual(calculator(0, 0, "divide"), "Error: Division by zero")

    def test_invalid_operation(self):
        self.assertEqual(calculator(10, 5, "modulo"), "Error: Invalid operation")
        self.assertEqual(calculator(10, 5, ""), "Error: Invalid operation")
        self.assertEqual(calculator(10, 5, None), "Error: Invalid operation")

    def test_float_inputs(self):
        self.assertEqual(calculator(2.5, 0.5, "add"), 3.0)
        self.assertEqual(calculator(5.5, 2.5, "subtract"), 3.0)
        self.assertEqual(calculator(2.0, 3.0, "multiply"), 6.0)
        self.assertEqual(calculator(7.5, 2.5, "divide"), 3.0)

if __name__ == "__main__":
    unittest.main()