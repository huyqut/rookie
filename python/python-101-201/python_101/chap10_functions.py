# FUNCTIONS


def a_function():
    """
    Define a function
    :return: None 
    """
    print("hello world!")

a_function()


def pass_func():
    """
    This is an empty function. Applied when outlining structures
    :return: None 
    """
    pass


def arg_func(a, b):
    """
    Function with arguments
    :param a: Number
    :param b: Number
    :return: Number = sum of a and b
    """
    return a + b

print(arg_func(1, 2))
print(arg_func(a = 1, b = 2))  # You can also use keyword arguments for clarification

# Arguments in Python are not obligatory
# If an argument is missing, its value inside function is None
try:
    print(arg_func(1))  # Missing b = except
except:
    print("Missing b")
# If there are more arguments than provided functions, it is dismissed
try:
    print(arg_func(3, 4, 5))  # Redundant is dismissed
except:
    print("Too many arguments")

# Default value for an argument function. If there is a default value of a previous argument,
# later arguments must also be provided with default values


def default_arg(a = 1, b = 2):
    return a + b

print(default_arg())  # a = 1, b = 2


def partial_default_arg(a, b, c = 1, d = 2):
    return a + b + c + d


# Hinting types: both arguments and return can be hinted


def hint_arg(a: list, b: set, c: dict) -> list:
    """
    :param a: list 
    :param b: set
    :param c: dict
    :return: list
    """
    v = []
    for x in a:
        for y in b:
            for z in c.keys():
                v.append(x + y + z)
    return v

print(hint_arg([1, 2, 3], {1, 2, 3}, {1: '1', 2: '2'}))

# Infinite arguments: *args (only need '*', after that can be anything: *values, *keys, *etc, ...)
# *args is a tuple type


def inf_arg(*args):
    print(args)

inf_arg(0, 1, 2, 'a', 'b', {1, 2, 3}, [4, 5, 6])


# Infinite keyword arguments: **kwargs (only need '**', after that can be anything: **values, **keys, **etc, ...)
# **kwargs is a dict type


def inf_kwarg(**kwargs):
    print(kwargs)

inf_kwarg(first_name = 'Huy', last_name = 'Tran', age = 18, girls = [1, 2, 3], memory = {1: '2', 3: '4'})



