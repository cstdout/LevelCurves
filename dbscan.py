from math import sqrt


class Point:
    NOISE_CLUSTER_ID = -1
    NOT_ASSIGNED_TO_CLUSTER = -2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.is_visited = False
        self.cluster_id = Point.NOT_ASSIGNED_TO_CLUSTER


def distance(q, p):
    dx = p.x - q.x
    dy = p.y - q.y
    return sqrt(dx * dx + dy * dy)


def get_point_neighbours(all_points, point, eps):
    neighbours = []
    for q in all_points:
        if distance(point, q) <= eps:
            neighbours.append(q)
    return neighbours


def dbscan(all_points, eps, min_pts):
    cluster_id = -1
    for point in all_points:
        if not point.is_visited:
            point.is_visited = True
            point_neighbours = get_point_neighbours(all_points, point, eps)
            if len(point_neighbours) < min_pts:
                point.cluster_id = Point.NOISE_CLUSTER_ID
            else:
                cluster_id += 1
                point.cluster_id = cluster_id
                seed_set = []
                for p in point_neighbours:
                    seed_set.append(p)

                for q in seed_set:
                    if not q.is_visited:
                        q.is_visited = True
                        point_neighbours.clear()
                        point_neighbours = get_point_neighbours(all_points, q, eps)
                        if len(point_neighbours) >= min_pts:
                            for p in point_neighbours:
                                seed_set.append(p)

                    if q.cluster_id == Point.NOT_ASSIGNED_TO_CLUSTER:
                        q.cluster_id = cluster_id
                seed_set.clear()
    res = []
    for p in all_points:
        res.append(p.cluster_id)
    return res
