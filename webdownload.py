#!/usr/bin/env python3

from urllib.request import urlopen

url = 'https://www.google.com/'

response = urlopen(url)
webContent = response.read()

f = open('obo-t17800628-33.html', 'w')
f.write(webContent)
f.close

