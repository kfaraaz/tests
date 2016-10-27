import argparse
parser = argparse.ArgumentParser(description='This script takes a URL as input')
parser.add_argument('-u','--ur',action='store',dest='url',default=None,help='<Required> url link',required=True)
results = parser.parse_args()
url = results.url
print url
