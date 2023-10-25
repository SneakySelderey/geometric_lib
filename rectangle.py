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


    def test_perimeter_negative_or_zero_values(self):
        """Test function for negative or zero values perimeter case
        """
        for x in [-1, 0, 5]:
            for y in [-1, 0, 5]:
                if [x, y] != [5, 5]:
                    self.assertRaises(ValueError, get_rectangle_perimeter, x, y)


    def test_area_negative_or_zero_values(self):
        """Test function for negativeor zero values area case
        """
        for x in [-1, 5, 0]:
            for y in [-1, 5, 0]:
                if [x, y] != [5, 5]:
                    self.assertRaises(ValueError, get_rectangle_area, x, y)


    def test_area_float_values(self):
        """Test function for float values area case
        """
        self.assertAlmostEqual(get_rectangle_area(4.23, 6.82), 28.8486, 4)


    def test_perimeter_float_values(self):
        """Test function for float values perimeter case
        """
        self.assertEqual(get_rectangle_perimeter(4.23, 6.82), 22.1, 4)


    def test_area_int_values(self):
        """Test function for int values area case
        """
        self.assertEqual(get_rectangle_area(4, 6), 24)


    def test_perimeter_int_values(self):
        """Test function for int values perimeter case
        """
        self.assertEqual(get_rectangle_perimeter(4, 6), 20)


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
