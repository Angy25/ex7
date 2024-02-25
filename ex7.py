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
    """
    calculates x*y, with running time O(log y)
    mult(x: float, y: int) -> float
    """
    if y == 0:
        return 0
    z = log_mult(x, divide_by_2(y))
    if y == 1:
        return x
    elif is_odd(y):
        return add(add(z, z), x)
    return add(z, z)


def up(x, b, c, step):
    """

    :param x: 
    :param b: 
    :param c: 
    :param step: 
    :return: 
    """
    # stop condition
    if c * b > x:
        return c, step

    # recursion
    return up(x, b, c + step, 2 * step)


def zigzag(x, b, c, step):
    """
    
    :param x:
    :param b:
    :param c: 
    :param step: 
    :return: 
    """
    # stop condition
    if c * b == x:
        return c
    if not step:
        return None
    
    # recursion
    if c * b > x:
        return zigzag(x, b, c - step, divide_by_2(step))
    
    if c * b < x:
        return zigzag(x, b, c + step, divide_by_2(step))
        

def division(x, b):
    """
    """
    step = 1
    c = 1
    c, step = up(x, b, c, step)
    
    step = divide_by_2(divide_by_2(step))
    return zigzag(x, b, c, step)


def is_power(b: int, x: int) -> bool:
    """return True if there is an integer n such as b^n = x, and False otherwise, with running time O(log b * lox x)"""

    # stop condition
    if not x:
        return False
    if b > x:
        return False
    if b == 1:
        return x == 1
    if b == x:
        return True

    # recursion
    return is_power(b, division(x, b))


if __name__ == '__main__':
    print(is_power(3, 28))
