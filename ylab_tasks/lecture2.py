"""Solution of task from the second lecture"""
from itertools import combinations
from math import hypot


def distance(p1: tuple, p2: tuple) -> float:
    """Calculates the distance between 2 points"""
    return hypot(p2[0] - p1[0], p2[1] - p1[1])


def shortest_route(points: tuple) -> str:
    """Calculates the shortest route between all points"""
    number_of_points = len(points)

    if number_of_points > 7:
        return "Too many points. Max number of points 7"
    elif number_of_points <= 1:
        return "Too few points. Min number of points 2"

    end_point = points[0]
    shortest = []

    for route in combinations(points[1:], number_of_points - 1):
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
