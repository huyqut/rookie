# DECORATOR
# A decorator is a function that accepts 1 and only 1 argument that is another function
# (or a callback) and improve it better (decorate)
import logging


def log_decorator(func):

    def wrapper(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        logfile = logging.FileHandler(f'./data/chap25_{name}.log')
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        logfile.setFormatter(formatter)
        logger.addHandler(logfile)

        logger.warning(f"Running function {name}")
        result = func(*args, **kwargs)
        logger.info(f"Result: {result}")
        return result

    return wrapper


@log_decorator
def square(number):
    return number * number

value = square(4)
print(value)

# Built-in Decorators

# @staticmethod
# Method can be used as Class.method() without a class instance

# @classmethod
# Instead of 'self' object, the class of the object is passed

# @property
# Call the function the same way as an attribute (without any argument)


class Math:

    def __init__(self):
        self._award = "Ngo Bao Chau"

    @staticmethod
    def halve(number):
        return number // 2

    @classmethod
    def crazy(cls, number):
        print(cls)
        return str(number)

    def wolo(self, number):
        print(self)
        return number + 1

    @property
    def field_award(self):
        return self._award

    @field_award.setter
    def field_award(self, nominee: str):
        self._award = nominee

print(Math.halve(5))
mat = Math()
print(mat.crazy(9))
print(mat.wolo(11))
print(mat.field_award)
mat.field_award = "Tran Quang Huy"
print(mat.field_award)
