from functools import partial
import pytest


class Operations:

    @staticmethod
    def add(a: int, b: int):
        return a + b

    @staticmethod
    def sub(a: int, b: int):
        return a - b

    @staticmethod
    def div(a: int, b: int):
        assert b > 0, "Zero division error!"
        return a / b

    @staticmethod
    def mul(a: int, b: int):
        return a * b

    @staticmethod
    def power(base: int, exp: int):
        assert exp != 0, "Zero exponent error!"
        return base ** exp

    @staticmethod
    def dob(a: int, b: int):
        return a + (b * 2)

    @staticmethod
    def squared(a: int, b: int):
        return a + b ** 2

    @staticmethod
    def cube(a: int, b: int):
        cube_operand = partial(Operations.power, exp=3)
        return a + cube_operand(b)

    @staticmethod
    def inverse_multiplicative(a: int, b: int):
        assert b > 0, "Zero division error!"
        #  Another way is to exponent the operator to -1
        #  x ^ -1 = 1 / x
        #  minus_one_operator = partial(Operations.power, exp=-1)
        return a + Operations.div(1, b)


    @staticmethod
    def martin_chaia_function(arr: [], action):
        total: int = 0
        for i in arr:
            total = action(total, i)
        return total
