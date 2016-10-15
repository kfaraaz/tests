# To run this script, run it as shown below
# python getJSONDataFromURL.py -u https://commondatastorage.googleapis.com/ckannet-storage/2012-02-07T223547/PTStateBudget2012.json
# Do NOT forget to pass the URL as an input

import argparse
import json
from urllib import urlopen


def getJSONDataFromURL():
    """ Read JSON data from URL and write it to a file"""
    parser = argparse.ArgumentParser(
        description='This script takes a URL as an input')
    parser.add_argument(
        '-u',
        '--ur',
        action='store',
        dest='url',
        default=None,
        help='<Required> url link',
        required=True)
    results = parser.parse_args()
    url = results.url
    u = urlopen(url)
    data = u.read()
    with open('data.json', 'w') as f:
        json.dump(json.JSONDecoder().decode(data), f)


if __name__ == "__main__":
    getJSONDataFromURL()
