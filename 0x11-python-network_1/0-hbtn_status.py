#!/usr/bin/python3
"""script that fetches 'https://alx-intranet.hbtn.io/status' """
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
print("""Body response:\n    - type: {}\n    - content: {}
    - utf8 content: {}""".format(type(html), html, html.decode('utf-8')))
