"""Solutions of tasks from the first lecture"""
import socket
import struct
from urllib.parse import urlparse


def decomposer(num: int, divider: int) -> int:
    """Counts the number of specified prime divisors in a number"""
    count = 0
    while num >= divider:
        if not num % divider:
            count += 1
            num /= divider
        else:
            return count
    return count


#Решение задачи №1
def domain_name(url: str) -> str:
    """Gets the domain name from the link"""
    parsed_url = urlparse(url)
    if not parsed_url.hostname:
        return url.split('.')[1]
    host = parsed_url.hostname.split('.')
    if host[0] == 'www':
        return host[1]
    else:
        return host[0]


#Решение задачи №2
def int32_to_ip(int32: int) -> str:
    """Converts a 32bit number to an IPv4 address"""
    structed_num = struct.pack("!I", int32)
    ip = socket.inet_ntoa(structed_num)
    return ip


#Решение задачи №3
def zeros(n: int) -> int:
    """Returns the number of trailing zeros of the factorial"""
    deuces = 0
    fives = 0
    for i in range(1, n + 1):
        if not i % 2:
            deuces += decomposer(i, 2)
        if not i % 5:
            fives += decomposer(i, 5)
    return min(deuces, fives)
