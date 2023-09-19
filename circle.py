import math


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
