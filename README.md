# Conectivity checker

With this module you can check the conectivity of any url, just put the url and the function return the status.

## Usage

To use this module, just need to copy the module to your proyect and then import the module in your code when you need it
```python
from checker import conectivity_checker

# initial parameters
input_url = input('Insert the url to check: ')

# just use when need it, recomend use try/except becasuse if any error
# retun error code it's look better
try:
    conectivity_checker(input_url)
except Exception as e:
    print(f"Oops.. something it's wrong \nPlease, check this error: {e}")
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

This is a practice proyect so, maybe have changes in the future