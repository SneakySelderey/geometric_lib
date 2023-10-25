import unittest


class SquareTestCase(unittest.TestCase):
    """Class of tests for square.py functions

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
            if x != 5:
                self.assertRaises(ValueError, get_square_area, x)


    def test_area_negative_or_zero_values(self):
        """Test function for negativeor zero values area case
        """
        for x in [-1, 5, 0]:
            if x != 5:
                self.assertRaises(ValueError, get_square_area, x)


    def test_area_float_values(self):
        """Test function for float sides values case
        """
        self.assertAlmostEqual(get_square_area(6.82), 46.5124, 4)


    def test_perimeter_float_values(self):
        """Test function for float values perimeter case
        """
        self.assertEqual(get_square_perimeter(6.82), 27.28, 4)


    def test_area_int_values(self):
        """Test function for int values area case
        """
        self.assertEqual(get_square_area(6), 36)


    def test_perimeter_int_values(self):
        """Test function for int values perimeter case
        """
        self.assertEqual(get_square_perimeter(6), 24)



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
