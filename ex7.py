from ex7_helper import *


def mult(x, y):
    """
    calculates x*y
    mult(x: int/float, y: int) -> int/float
    """
    if y == 0:
        return 0
    y = subtract_1(y)
    return add(x, mult(x, y))


def is_even(n: int) -> bool:
    if n == 1:
        return False
    if n == 2:
        return True
    n = subtract_1(subtract_1(n))
    return is_even(n)


def log_mult(x, y):
    if y == 0:
        return 0
    z = log_mult(x, y//2)
    z = subtract_1(z)
    if is_odd(y):
        return add(add(z, z), x)
    else:
        return add(z + z)

