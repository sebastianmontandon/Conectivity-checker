import urllib.request as urllib
from urllib.parse import urlparse, urlunparse
from rich import print

def conectivity_checker(url:str):
    print("Checking...")
    parse_url = urlparse(url)
    if parse_url.scheme == '' and parse_url.netloc == '':
        parse_url = parse_url._replace(scheme="https", netloc=parse_url.path, path='')
        result = urlunparse(parse_url)
    else:
        parse_url = parse_url._replace(scheme="https")
        result = urlunparse(parse_url)
    response = urllib.urlopen(result)
    print(f"Conected to {result} succesfully, the response code was {response.getcode()}")