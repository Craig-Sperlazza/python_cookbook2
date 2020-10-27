# https://www.youtube.com/watch?v=NTLAuvfJwmE&feature=emb_logo

#this is probably the worst way to try to do this but it is with standard library

#HTTP GET and POST Request with standard library

import urllib.request

#open URL with string
response = urllib.request.urlopen('https://www.devdungeon.com')
html = response.read()
print(html)

print("----------------------------------------------------------------------------")
#Or prebuild the request
request = urllib.request.Request('https://www.devdungeon.com')
request.add_header('User-Agent', 'Not Firefox')
response = urllib.request.urlopen(request)
print(response.read())

