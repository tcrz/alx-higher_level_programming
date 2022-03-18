#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
using requests"""
if __name__ == "__main__":
    import requests

    r = requests.get("https://alx-intranet.hbtn.io/status")
    print('Body response:\n\t- type: {}\n\t- content: {}'
          .format(type(r.text), r.text))
