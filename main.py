from rich import print
from checker import conectivity_checker

input_url = input('Insert the url to check: ')

try:
    conectivity_checker(input_url)
except Exception as e:
    print(f"Oops.. something it's wrong \nPlease, check this error: {e}")