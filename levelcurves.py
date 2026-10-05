def my_func(x, y):
    return (x ** 2) + (x * y) + (y ** 2)
    # return ((x * y) ** 3) + x * y
    # return cos(x) * sin(y)


def function_at_level(x, y, z0, func):
    return func(x, y) - z0
