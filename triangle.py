def area(a, h):
    """return an area of given triangle

    Args:
        a (int/float): side of the triangle
        h (int/float): height of the triangle that drops on side "a"

    Returns:
        int/float: area of the triangle
    """
    return a * h / 2 

def perimeter(a, b, c):
    """return a perimeter of given triangle

    Args:
        a (int/float): first side of the triangle
        b (int/float): second side of the triangle
        c (int/float): third side of the triangle

    Returns:
        int/float: perimeter of the triangle
    """
    return a + b + c 
