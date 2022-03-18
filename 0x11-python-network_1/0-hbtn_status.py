#!/usr/bin/python3
"""script that fetches 'https://alx-intranet.hbtn.io/status' """
from urllib import request

""" get status code """


with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    data = resp.read()

print("Body response:")
print('\t- type: {}'.format(type(data)))
print('\t- content: {}'.format(data))
print('\t- utf8 content: {}'.format(data.decode('UTF8')))
