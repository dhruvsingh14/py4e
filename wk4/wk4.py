import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# opens connection
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# runs through each line of url
for line in fhand:
    print(line.decode().strip())
