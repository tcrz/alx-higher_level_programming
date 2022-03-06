#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument:

    - script takes 4 arguments: mysql username, mysql password, database name
    and state name searched (no argument validation needed)
    - uses the module MySQLdb (import MySQLdb)
    - script connects to a MySQL server running on localhost at port 3306
    - uses format() to create the SQL query with the user input
    - Results are sorted in ascending order by states.id
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    argv = (sys.argv)[1:]
    db = MySQLdb.connect(user=argv[0], passwd=argv[1], db=argv[2])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY states.id ASC"
                .format(argv[3]))
    rows = cur.fetchall()
    for row in rows:
        if argv[3] == row[1]:
            print(row)
