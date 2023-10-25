import unittest
import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    """Class of tests for circle.py functions

    Args:
        unittest (TestCase): parent class
    """
    def set_up(self):
        """Set up fucntion
        """
        pass


    def test_area_zero_rad(self):
        """Test function for zero radius area case
        """
        self.assertEqual(circle.get_circle_area(0), 0)


    def test_circumference_zero_rad(self):
        """Test function for zero radius circumference case
        """
        self.assertEqual(circle.get_circle_perimeter(0), 0)


    def test_area_negative_rad(self):
        """Test function for negative radius area case
        """
        self.assertRaises(ValueError, circle.get_circle_area(-1))


    def test_circumference_negative_rad(self):
        """Test function for negative radius circumference case
        """
        self.assertRaises(ValueError, circle.get_circle_perimeter(-1))


    def test_area_float_rad(self):
        """Test function for float radius area case
        """
        self.assertAlmostEqual(circle.get_circle_area(3.57), 40.039284, 6)


    def test_circumference_float_rad(self):
        """Test function for float radius circumference case
        """
        self.assertAlmostEqual(circle.get_circle_perimeter(3.57), 22.43097, 5)
