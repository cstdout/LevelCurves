from math import sqrt


class Point:
    NOISE_CLUSTER_ID = -1
    NOT_ASSIGNED_TO_CLUSTER = -2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.is_visited = False
        self.cluster_id = Point.NOT_ASSIGNED_TO_CLUSTER


def distance(q: Point, p: Point):
    dx = p.x - q.x
    dy = p.y - q.y
    return sqrt(dx * dx + dy * dy)
