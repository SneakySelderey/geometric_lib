import unittest


class RectangleTestCase(unittest.TestCase):
    """Class of tests for rectangle.py functions

    Args:
        unittest (TestCase): parent class
    """
    def set_up(self):
        """Set up fucntion
        """
        pass


    def test_area_zero_sides(self):
        """Test function for zero sides area case
        """
        self.assertEqual(get_rectangle_area(0, 0), 0)


    def test_perimeter_zero_sides(self):
        """Test function for zero sides perimeter case
        """
        self.assertEqual(get_rectangle_perimeter(0, 0), 0)


    def test_area_zero_side(self):
        """Test function for zero side area case
        """
        self.assertEqual(get_rectangle_area(0, 5), 0)
        self.assertEqual(get_rectangle_area(5, 0), 0)


    def test_perimeter_zero_side(self):
        """Test function for zero side perimeter case
        """
        self.assertEqual(get_rectangle_perimeter(0, 5), 0)
        self.assertEqual(get_rectangle_perimeter(5, 0), 0)


    def test_area_float_sides(self):
        """Test function for float sides area case
        """
        self.assertAlmostEqual(get_rectangle_area(4.23, 6.82), 28.8486, 4)


    def test_perimeter_float_sides(self):
        """Test function for float sides perimeter case
        """
        self.assertEqual(get_rectangle_perimeter(4.23, 6.82), 22.1, 4)


def get_rectangle_area(a, b):
    """Returns an area of given rectangle

    Args:
        a (int/float): one side of the rectangle
        b (int/float): neighboring side of the rectangle

    Returns:
        int/float: area of the rectangle
    """
    return a * b 

def get_rectangle_perimeter(a, b):
    """Returns a perimeter of given rectangle

    Args:
        a (int/float): one side of the rectangle
        b (int/float): neighboring side of the rectangle

    Returns:
        int/float: perimeter of the rectangle
    """
    return 2 * (a + b) 
