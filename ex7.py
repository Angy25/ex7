from typing import Any

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


def reverse(s: str) -> str:
    """
    gets a string, the characters are in some order, the function crates a string with those characters in the opposite
    order.
    :param s: str
    :return: str
    """

    # stop condition
    if len(s) == 1:
        return s

    # recursion
    return append_to_end(reverse(s[1::]), s[0])


def play_hanoi(hanoi: Any, n: int, src: Any, dest: Any, temp: Any):
    """

    :param dest:
    :param hanoi:
    :param n:
    :param src:
    :param temp:
    :return:
    """
    # recursion: move triangle to temp from src
    play_hanoi(hanoi, n - 1, src, temp, dest)

    # move base to destination (the pole which is not src or temp)
    hanoi.move(src, dest)

    # move triangle on top of base
    play_hanoi(hanoi, n - 1, temp, dest, src)


def count_1(num: int) -> int:
    """counts how many times the digit 1 appears in num"""

    # stop condition
    if num == 1:
        return 1
    if num == 0:
        return 0

    # recursion
    return add(count_1(num // 10), num % 10 == 1)


def number_of_ones(n: int) -> int:
    # stop condition
    if n < 10:
        return 1

    # recursion
    return add(count_1(n), number_of_ones(subtract_1(n)))


def compare_2d_lists(l1, l2):
    """
    Recursively compares multy-dimensional lists.
    :param l1: (list): First 2D list for comparison.
    :param l2: (list): Second 2D list for comparison.
    :return: True if the lists are equal, False otherwise.
    """

    if len(l1) != len(l2):  # Check if the lengths of the lists are equal
        return False

    if len(l1) == len(l2) == 0:  # Spacial case of empty list
        return True

    i = subtract_1(len(l1))  # Start from the last element
    if isinstance(l1[i], list) and isinstance(l1[i], list):  # If elements are lists, recursively compare them
        if not compare_2d_lists(l1[i], l2[i]):
            return False
        if compare_2d_lists(l1[i], l2[i]):
            i = subtract_1(i)  # Move to the previous element for comparison
            if i == -1:
                return True
            return compare_2d_lists(l1[i], l2[i])

    else:  # Entered the most inner list (list of ints or empty list)
        if l1[i] != l2[i]:  # Check if the current elements are equal
            return False
        if l1[i] == l2[i]:
            i = subtract_1(i)  # Move to the previous element for comparison
            if i == -1:
                return True
            return compare_2d_lists([l1[i]], [l2[i]])

def magic_list(n):





if __name__ == '__main__':
    print(compare_2d_lists([[1, 3], [4]], [[1, 3], [4]]))



