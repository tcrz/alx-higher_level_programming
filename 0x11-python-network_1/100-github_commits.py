#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""
if __name__ == "__main__":
    import requests
    import sys

    r2 = requests.get(
        'https://api.github.com/repos/{}/{}/commits?per_page=10'
        .format(sys.argv[1], sys.argv[2]))
    data = r2.json()
    if len(data) > 2:
        dates = []
        for i in range(len(data)):
            raw_data = data[i]
            dates.append((raw_data.get('commit').get('author').get('date')))
        dates = sorted(dates, reverse=True)
        for d in dates:
            for i in range(len(data)):
                raw_data = data[i]
                if d == raw_data.get('commit').get('author').get('date'):
                    print(raw_data.get('sha')+':',
                          raw_data.get('commit').get('author').get('name'))
