"""Solutions of tasks from the first lecture"""
from urllib.parse import urlparse


def domain_name(url: str) -> str:
    """Gets the domain name from the link"""
    if url.startswith('www'):
        return url.split('.')[1]
    host = urlparse(url).hostname.split('.')
    return host[0]
