#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""
if __name__ == "__main__":
    import requests
    import sys

    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[2], sys.argv[1]))
    if r.status_code >= 400:
        print('None')
    else:
        for com in r.json()[:10]:
            print("{}: {}".format(com.get('sha'),
                                  com.get('commit').get('author').get('name')))
