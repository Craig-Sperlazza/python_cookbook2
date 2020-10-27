# https://docs.python.org/3/library/urllib.parse.html

from urllib.parse import urlparse, urlunparse

parsed_url = urlparse(
    'https://www.devdungeon.com/test/node/1?q=5&x=that#test_fragment')

print(parsed_url)
print(parsed_url.scheme)
print(parsed_url.netloc)
print(parsed_url.path)
print(parsed_url.params)
print(parsed_url.query)
print(parsed_url.fragment)

new_url = urlunparse((
        'https',               # Scheme
        'www.devdungeon.com',  # Netloc
        '/archive',            # Path
         None,                  # Params
        'q=5&x=that',          # Query (use urlencode())
        'test_fragment'))      # Fragment
print(new_url)
