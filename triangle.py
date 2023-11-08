import unittest


class TriangleTestCase(unittest.TestCase):
    """Class of tests for rectangle.py functions

    Args:
        unittest (TestCase): parent class
    """
    def set_up(self):
        """Set up fucntion
        """
        pass


    def test_area_negative_or_zero_side_or_height(self):
        """Test function for negative or zero side or height area case
        """
        for x in [-1, 0, 5]:
            for y in [-1, 0, 5]:
                if [x, y] != [5, 5]:
                    self.assertRaises(ValueError, get_triangle_area, x, y)


    def test_perimeter_negative_or_zero_side(self):
        """Test function for negative or zero sides perimeter case
        """
        for x in [-1, 0, 5, 10]:
            for y in [-1, 0, 5, 10]:
                for z in [-1, 0, 5, 10]:
                    if x * y * z == 0:
                        self.assertRaises(ValueError, get_triangle_perimeter, x, y, z)


    def test_area_float_sides_height(self):
        """Test function for float sides and float height area case
        """
        self.assertAlmostEqual(get_triangle_area(6.82, 3.57), 12.1737, 4)


    def test_perimeter_float_sides(self):
        """Test function for float sides perimeter case
        """
        self.assertEqual(get_triangle_perimeter(6.82, 3.57, 7.25), 17.64)


    def test_area_int_values(self):
        """Test function for generic values area case
        """
        self.assertEqual(get_triangle_area(10, 4), 20)


    def test_perimeter_int_values(self):
        """Test function for generic values perimeter case
        """
        self.assertEqual(get_triangle_perimeter(10, 4, 6), 20)


def get_triangle_area(a, h):
    """Returns an area of given triangle

    Args:
        a (int/float): side of the triangle
        h (int/float): height of the triangle that drops on side "a"

    Returns:
        float: area of the triangle
    """
    return a * h / 2

def get_triangle_perimeter(a, b, c):
    """Returns a perimeter of given triangle

    Args:
        a (int/float): first side of the triangle
        b (int/float): second side of the triangle
        c (int/float): third side of the triangle

    Returns:
        int/float: perimeter of the triangle
    """
    return a + b + c
