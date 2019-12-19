
class Operations:

    @staticmethod
    def add(a: int):
        return +a

    @staticmethod
    def sub(a: int):
        return -a

    @staticmethod
    def power(base: int, exp: int):
        assert exp != 0, "Zero exponent error!"
        if exp < 0:
            assert base != 0, "Zero division error!"
        return base ** exp

    @staticmethod
    def dob(a: int):
        return a * 2

    @staticmethod
    def squared(a: int):
        return a ** 2

    @staticmethod
    def cube(a: int):
        return Operations.power(base=a, exp=3)

    @staticmethod
    def inverse_multiplicative(a: int):
        assert a > 0, "Zero division error!"
        #  Another way is to exponent the operator to -1
        #  x ^ -1 = 1 / x
        #  minus_one_operator = partial(Operations.power, exp=-1)
        return 1 / a

    @staticmethod
    def martin_chaia_function(arr: list, action):
        total: int = 0
        for i in arr:
            total = total + action(i)
        return total
