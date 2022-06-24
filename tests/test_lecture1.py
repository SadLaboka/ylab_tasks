from ylab_tasks.lecture1 import (
    bananas, count_find_num, domain_name, int32_to_ip, zeros)


def test_domain_name():
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
    assert domain_name("https://www.cnet.com") == "cnet"
    assert domain_name("http://www.zombie-bites.com") == "zombie-bites"


def test_int32_to_ip():
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"


def test_zeros():
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(12) == 2
    assert zeros(30) == 7


def test_bananas():
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--",
                                    "-b--anana", "b-a--nana",
                                    "-banan--a", "b-ana--na",
                                    "b---anana", "-bana--na",
                                    "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na",
                                   "b--anana", "banana--", "banan--a"}


def test_count_find_num():
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []
