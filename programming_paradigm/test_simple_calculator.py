import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Basic addition tests
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Test with negative numbers
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        
        # Test with decimal numbers
        self.assertEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=10)
        
        # Test with larger numbers
        self.assertEqual(self.calc.add(1000, 2000), 3000)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Basic subtraction tests
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        
        # Test with negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        
        # Test with decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.3), 3.2)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=10)
        
        # Test with larger numbers
        self.assertEqual(self.calc.subtract(1000, 300), 700)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Basic multiplication tests
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(2, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(1, 7), 7)
        
        # Test with negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(0, -5), 0)
        
        # Test with decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=10)
        
        # Test with larger numbers
        self.assertEqual(self.calc.multiply(100, 50), 5000)

    def test_division(self):
        """Test the division method."""
        # Basic division tests
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        self.assertEqual(self.calc.divide(1, 1), 1.0)
        
        # Test division resulting in decimals
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333, places=10)
        
        # Test with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        
        # Test with decimal numbers
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)
        self.assertEqual(self.calc.divide(0.6, 0.2), 3.0)
        
        # Test division of zero
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)

    def test_division_by_zero(self):
        """Test division by zero cases."""
        # Test division by zero returns None
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(3.14, 0))

    def test_edge_cases(self):
        """Test additional edge cases for all operations."""
        # Test with very large numbers
        large_num = 999999999999
        self.assertEqual(self.calc.add(large_num, 1), 1000000000000)
        self.assertEqual(self.calc.subtract(large_num, 1), 999999999998)
        
        # Test with very small decimal numbers
        small_num = 0.000001
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 0.000002, places=6)
        self.assertAlmostEqual(self.calc.multiply(small_num, 2), 0.000002, places=6)

if __name__ == '__main__':
    unittest.main()