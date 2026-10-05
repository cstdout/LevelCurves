def my_func(x, y):
    return (x ** 2) + (x * y) + (y ** 2)
    # return ((x * y) ** 3) + x * y
    # return cos(x) * sin(y)


def function_at_level(x, y, z0, func):
    return func(x, y) - z0


# TODO return roots
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


def solver(x0, z0, y_min, y_max, func, is_increasing=False):
    L = y_min
    R = y_max
    EPS = 1e-6
    mid = 0
    while abs(L - R) > EPS:
        mid = (L + (R - L) / 2.0)
        val = function_at_level(x0, mid, z0, func)
        if is_increasing and val < 0 or not is_increasing and val > 0:
            L = mid
        else:
            R = mid
    return mid


def find_intersection_points(x_min, x_max, y_min, y_max, z0, func, x_step=0.1, y_step=0.5):
    intersection_points = []

    x0 = x_min
    EPS = 1e-6

    change_sign_intervals = []
    while x0 < x_max:
        change_sign_intervals = get_intervals_where_function_changes_its_sign(x0, y_min, y_max, y_step, z0, func)
        for interval in change_sign_intervals:
            y = solver(x0, z0, interval[0], interval[1], func, interval[2])
            if abs(function_at_level(x0, y, z0, func)) <= EPS:
                intersection_points.append((x0, y))
        x0 += x_step

    return intersection_points


def draw_points(points):
    fig, ax = plt.subplots(figsize=(8, 8))

    x_min = -5
    x_max = 5
    y_min = -5
    y_max = 5

    # Set limits
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    # Grid
    ax.grid(True, linestyle="--", color="lightgray")

    # X-axis with arrow
    ax.annotate("", xy=(x_max, 0), xytext=(x_min, 0), arrowprops=dict(arrowstyle="->",
                                                                      color="black",
                                                                      linewidth=1.5))

    # Y-axis with arrow
    ax.annotate("", xy=(0, y_max), xytext=(0, y_min), arrowprops=dict(arrowstyle="->",
                                                                      color="black",
                                                                      linewidth=1.5))

    # Axis labels
    ax.text(x_max - 0.5, 0.4, "X", fontsize=14)
    ax.text(0.4, y_max - 0.5, "Y", fontsize=14)

    # Ticks
    ax.set_xticks(range(x_min, x_max + 1))
    ax.set_yticks(range(y_min, y_max + 1))

    for p in points:
        ax.scatter(p[0], p[1], color="red", s=2, zorder=5)

    # Equal proportions
    ax.set_aspect("equal")

    plt.show()


if __name__ == "__main__":
    points = find_intersection_points(-5, 5, -5, 5, 0.5, my_func)
    draw_points(points)
