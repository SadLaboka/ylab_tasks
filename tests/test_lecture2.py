from ylab_tasks.lecture2.task1 import distance, shortest_route


def test_distance():
    assert distance((0, 0), (0, 0)) == 0
    assert distance((0, 0), (1, 0)) == 1


def test_shortest_route():
    points = ((1, 0), (2, 0), (3, 0), (4, 0), (5, 0))
    points2 = ((0, 2), (2, 5), (5, 2), (6, 6), (8, 3))
    points3 = ((0, 1), (1, 4), (4, 1), (5, 5), (7, 2))

    many_result = "Too many points. Max number of points 7"
    few_result = "Too few points. Min number of points 2"
    result = "(1, 0) -> (2, 0)[1.0] -> (3, 0)[1.0] -> (4, 0)" \
             "[1.0] -> (5, 0)[1.0] -> (1, 0)[4.0] = 8.0"
    result2 = "(0, 2) -> (2, 5)[3.6055512754639896] -> (6, 6)" \
              "[4.123105625617661] -> (8, 3)[3.6055512754639896] " \
              "-> (5, 2)[3.1622776601683795] -> (0, 2)[5.0] = " \
              "19.496485836714022"
    result3 = "(0, 1) -> (1, 4)[3.1622776601683795] -> (5, 5)[4.123105625617" \
              "661] -> (7, 2)[3.6055512754639896] -> (4, 1)[3.162277660168" \
              "3795] -> (0, 1)[4.0] = 18.05321222141841"

    assert shortest_route(((0, 0),)) == few_result
    assert shortest_route(points + ((6, 0), (7, 0), (8, 0))) == many_result
    assert shortest_route(points) == result
    assert shortest_route(points2) == result2
    assert shortest_route(points3) == result3
