#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""
if __name__ == "__main__":
    import requests

    r2 = requests.get(
        'https://api.github.com/repos/rails/rails/commits?per_page=10')
    data = r2.json()
    for i in range(len(data)):
        raw_data = data[i]
        print(raw_data.get('sha'),
              raw_data.get('commit').get('author').get('name'))
