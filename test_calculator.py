import unittest
import calculator

class TestCalculatorPartner2(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-5, -7), -12)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)
        self.assertEqual(calculator.subtract(3, 8), -5)
        self.assertEqual(calculator.subtract(-2, -3), 1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(2, 8), 3.0)
        self.assertEqual(calculator.logarithm(10, 100), 2.0)
        self.assertAlmostEqual(calculator.logarithm(3, 27), 3.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

if __name__ == '__main__':
    unittest.main()