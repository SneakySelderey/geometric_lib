import math
import unittest


class CircleTestCase(unittest.TestCase):
    """Class of tests for circle.py functions

    Args:
        unittest (TestCase): parent class
    """
    def set_up(self):
        """Set up fucntion
        """
        pass


    def test_area_negative_or_zero_value(self):
        """Test function for negative or zero radius area case
        """
        self.assertRaises(ValueError, get_circle_area, 0)
        self.assertRaises(ValueError, get_circle_area, -1)


    def test_circumference_negative_or_zero_rad(self):
        """Test function for negative or zero radius circumference case
        """
        self.assertRaises(ValueError, get_circle_perimeter, 0)
        self.assertRaises(ValueError, get_circle_perimeter, -1)


    def test_area_float_rad(self):
        """Test function for float radius area case
        """
        self.assertAlmostEqual(get_circle_area(3.57), 40.039284, 6)


    def test_circumference_float_rad(self):
        """Test function for float radius circumference case
        """
        self.assertAlmostEqual(get_circle_perimeter(3.57), 22.43097, 5)


    def test_area_int_rad(self):
        """Test function for int radius area case
        """
        self.assertAlmostEqual(get_circle_area(3), 28.274334, 6)


    def test_circumference_int_rad(self):
        """Test function for int radius area case
        """
        self.assertAlmostEqual(get_circle_perimeter(3), 18.84956, 6)


def get_circle_area(r):
    """Returns an area of given circle

    Args:
        r (int/float): radius of the circle

    Returns:
        int/float: area of the circle
    """
    return math.pi * r * r


def get_circle_perimeter(r):
    """Returns a circumference of given circle

    Args:
        r (int/float): radius of the circle

    Returns:
        int/float: circumference of the circle
    """
    return 2 * math.pi * r
