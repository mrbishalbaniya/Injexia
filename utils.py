from urllib.parse import urlparse

def parse_url(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.query
