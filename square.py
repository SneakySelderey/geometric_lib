import unittest


class SquareTestCase(unittest.TestCase):
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
        self.assertEqual(get_square_area(0), 0)


    def test_perimeter_zero_sides(self):
        """Test function for zero sides perimeter case
        """
        self.assertEqual(get_square_perimeter(0), 0)


    def test_area_float_sides(self):
        """Test function for float sides area case
        """
        self.assertAlmostEqual(get_square_area(6.82), 46.5124, 4)


    def test_perimeter_float_sides(self):
        """Test function for float sides perimeter case
        """
        self.assertEqual(get_square_perimeter(6.82), 27.28, 4)



def get_square_area(a):
    """Returns an area of given square

    Args:
        a (int/float): side of the square

    Returns:
        int/float: area of the square
    """
    return a * a


def get_square_perimeter(a):
    """Returns a perimeter of given square

    Args:
        a (int/float): side of the square

    Returns:
        int/float: perimeter of the square
    """
    return 4 * a
