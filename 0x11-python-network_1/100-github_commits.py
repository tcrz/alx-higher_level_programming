#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""
if __name__ == "__main__":
    import requests
    import sys

    r2 = requests.get(
        'https://api.github.com/repos/{}/{}/commits'
        .format(sys.argv[1], sys.argv[2]))
    data = r2.json()
    if len(data) > 2:
        for i in r2.json()[:10]:
            print(i.get('sha')+':',
                  i.get('commit').get('author').get('name'))
