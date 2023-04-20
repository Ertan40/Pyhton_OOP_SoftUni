class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for num in args[1:]:
            if num > 0:
                result /= num
        return result

    @staticmethod
    def subtract(*args):
        return args[0] - sum(args[1:])


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))