"""Solutions of tasks from the first lecture"""
import socket
import struct
from itertools import combinations
from math import log, prod
from urllib.parse import urlparse


# Решение задачи №1
def domain_name(url: str) -> str:
    """Gets the domain name from the link"""
    parsed_url = urlparse(url)
    if not parsed_url.hostname:
        return url.split('.')[1] if url.startswith('www') else url.split('.')[0]
    host = parsed_url.hostname.split('.')
    if host[0] == 'www':
        return host[1]
    else:
        return host[0]


# Решение задачи №2
def int32_to_ip(int32: int) -> str:
    """Converts a 32bit number to an IPv4 address"""
    structed_num = struct.pack("!I", int32)
    ip = socket.inet_ntoa(structed_num)
    return ip


# Решение задачи №3
def zeros(n):
    if n == 0:
        return 0
    top_limit = round(log(n, 5))
    sum = 0
    for i in range(1, top_limit + 1):
        divisor = 1
        for k in range(i):
            divisor *= 5
        sum += n // divisor
    return sum


# Решение задачи №4
def bananas(s: str) -> set:
    """Searches for all combinations of occurrences of a word in a string
     and replaces extra characters with '-' """
    banana = "banana"
    result = set()
    len_string = len(s)
    for i in combinations(range(len_string), len_string - len(banana)):
        letters_list = list(s)
        for c in i:
            letters_list[c] = '-'
        resulting_str = "".join(letters_list)
        if resulting_str.replace("-", "") == banana:
            result.add(resulting_str)
    return result


# Решение задачи №5
def count_find_num(primesL: list, limit: int) -> list:
    """Searches for all possible options
     for multiplying elements up to the limit and
     returns the number of options and the maximum"""
    min_number = prod(primesL)
    result = set()
    result.add(min_number)
    if min_number > limit:
        return []
    old_values = {min_number}
    while min_number <= limit:
        new_values = set()
        for i in old_values:
            for n in primesL:
                mul = i * n
                new_values.add(mul)
                if mul <= limit:
                    result.add(mul)
        min_number = min(new_values)
        old_values = {i for i in new_values if i < limit}
    return [len(result), max(result)]
