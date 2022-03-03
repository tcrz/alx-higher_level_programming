#!/usr/bin/python3
"""
Same requirememts as 2-my_filer_states.py but is safe from MySQL injections!
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    argv = (sys.argv)[1:]
    db = MySQLdb.connect(user=argv[0], passwd=argv[1], db=argv[2])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s ORDER BY states.id ASC",
                (argv[3],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
