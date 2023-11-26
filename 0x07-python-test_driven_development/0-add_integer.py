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
    if not isinstance(a, (int, float)) or not instance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)

	return a + b
        
