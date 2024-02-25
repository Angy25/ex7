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
    mult(x: int/float, y: int) -> int/float
    """
    if y == 0:
        return 0
    z = log_mult(x, divide_by_2(y))
    if y == 1:
        return x
    elif is_odd(y):
        return add(add(z, z), x)
    else:
        return add(z, z)


def calculate_mathematical_expression(num1, num2, math_oprt):
    """
    the function receives two number and calculates the mathematical operation between them
    :param num1: a number
    :param num2: also a number
    :param math_oprt: (str) name of the mathematical operation
    :return: the calculation
    """

    # Addition
    if math_oprt == "Addition":
        return num1 + num2

    # Subtraction
    if math_oprt == "Subtraction":
        return num1 - num2

    # Division
    if math_oprt == "Division":
        if num2 == 0:
            return None
        return num1 / num2

    # Multiplication
    if math_oprt == "Multiplication":
        return num1 * num2

    return None


def is_power(b: int, x: int) -> bool:  # TODO: is the running time O(log b * lox x) ???
    """return True if there is an integer n such as b^n = x, and False otherwise, with running time O(log b * lox x)"""
    if b == 1:  # check special case
        return x == 1
    if b > x:
        return False
    if b == x:
        return True
    return is_power(b, calculate_mathematical_expression(x, b, "Division"))  # is_power(b, x/b)


