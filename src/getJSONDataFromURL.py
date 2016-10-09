import sys
import json
from urllib import urlopen


def getJSONDataFromURL():
    """ Read JSON data from URL and write it to a file"""
    url = sys.argv[1]
    u = urlopen(url)
    data = u.read()
    with open('data.json', 'w') as f:
        json.dump(json.JSONDecoder().decode(data), f)


getJSONDataFromURL()
