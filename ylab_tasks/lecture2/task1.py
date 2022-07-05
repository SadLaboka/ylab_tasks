"""Solution of task from the second lecture"""
from itertools import permutations
from math import hypot


def distance(p1: tuple, p2: tuple) -> float:
    """Calculates the distance between 2 points"""
    return hypot(p2[0] - p1[0], p2[1] - p1[1])


def make_routes(points: tuple) -> set:
    """Creates paths and removes duplicates"""
    tmp_routes = set()
    routes = set()

    for route in permutations(points, len(points)):
        tmp_routes.add(route)
        if route[::-1] not in tmp_routes:
            routes.add(route)

    return routes


def shortest_route(points: tuple) -> str:
    """Calculates the shortest route between all points"""
    number_of_points = len(points)

    if number_of_points > 7:
        return "Too many points. Max number of points 7"
    elif number_of_points <= 1:
        return "Too few points. Min number of points 2"

    routes = make_routes(points[1:])
    end_point = points[0]
    shortest = []

    for route in routes:
        route_length = 0
        last_point = end_point
        result = f"{last_point}"

        for point in (route + (end_point, )):
            dist = distance(last_point, point)
            route_length += dist
            result += f" -> {point}[{dist}]"
            last_point = point

        if not shortest or shortest[0] > route_length:
            shortest = [route_length, result]

    return f"{shortest[1]} = {shortest[0]}"
