def my_func(x, y):
    return (x ** 2) + (x * y) + (y ** 2)
    # return ((x * y) ** 3) + x * y
    # return cos(x) * sin(y)


def function_at_level(x, y, z0, func):
    return func(x, y) - z0


def get_intervals_where_function_changes_its_sign(x0, y_min, y_max, y_step, z0, func):
    EPS = 1e-6
    intervals = []
    y0 = y_min
    current_val = function_at_level(x0, y0, z0, func)
    prev_val = current_val

    y0 += y_step
    while y0 < y_max:
        current_val = function_at_level(x0, y0, z0, func)
        if not (current_val > 0 and prev_val > 0 or current_val < 0 and prev_val < 0 or abs(current_val) <= EPS):
            intervals.append((y0 - y_step, y0, current_val > prev_val))

        prev_val = current_val
        y0 += y_step
    return intervals
