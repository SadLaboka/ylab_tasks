from ylab_tasks.lecture1 import domain_name, int32_to_ip, zeros


def test_domain_name():
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"


def test_int32_to_ip():
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"


def test_zeros():
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(12) == 2
    assert zeros(30) == 7
