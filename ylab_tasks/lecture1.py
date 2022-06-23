"""Solutions of tasks from the first lecture"""
import socket
import struct
from urllib.parse import urlparse


def domain_name(url: str) -> str:
    """Gets the domain name from the link"""
    if url.startswith('www'):
        return url.split('.')[1]
    host = urlparse(url).hostname.split('.')
    return host[0]


def int32_to_ip(int32: int) -> str:
    """Converts a 32bit number to an IPv4 address"""
    structed_num = struct.pack("!I", int32)
    ip = socket.inet_ntoa(structed_num)
    return ip
