#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the body
of the response(decoded in utf-8) by managing urllib.error.HTTPError exceptions
and print: Error code: followed by the HTTP status code
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
