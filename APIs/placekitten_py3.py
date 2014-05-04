#!/usr/bin/env python2

from urllib.request import urlopen

width = input("What width should the picture have? ")
height = input("What height should the picture have? ")

# Construct the URL
url = 'http://placekitten.com/' + width + '/' + height
kitten = urlopen(url).read()

kitten_file = open('kittens.jpeg', 'wb')
kitten_file.write(kitten)
kitten_file.close()

print("The kitten picture has been written to kittens.jpeg")
print("The URL for it is " + url)
