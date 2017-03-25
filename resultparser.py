#!/usr/bin/env python3
"""
Print out the toplist from a Neptron race

Download example:
curl http://results.neptron.se/webapi/sthtunnelruncitytunneln2017/results\?page\=0\&pageSize\=33251\&raceId\=99\&sortOrder\=Place > results.json

"""
import json
from datetime import datetime
from pprint import pprint


filename = 'results.json'


def extract_time(r):
    try:
        return datetime.strptime(r['netTime'], '%M:%S')
    except ValueError:
        return datetime.strptime(r['netTime'], '%H:%M:%S')


def print_runner(place, r):
    print('{:4d}  {} {} {:6d} {}'.format(
        place, r['time'], r['gender'], r['startNo'], r['name']))


def print_results(results, top):
    place = 0
    for runner in results[:top]:
        place += 1
        print_runner(place, runner)

data = json.load(open(filename))
results = data['results']

# Remove runners that did not finish
results = filter(lambda r: r['netTime'], results)
# Sort results
sortedresults = sorted(results, key=extract_time)

print_results(sortedresults, 50)
