#!/usr/bin/python3

def add_integer(a, b=98):
    """
    This defines an integer addition function
    Args:
        a (An int of float): The first number.
        b (An int or floa, optional): The Second number. Default is 98.
    Returns: An integer - The sum of a and b.
    Raises: TypeError: If a or b is not an integer or float.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
