#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa:

    - script takes 3 arguments: mysql username, mysql password and databasename
    - uses the module MySQLdb (import MySQLdb)
    - script should connect to a MySQL server running on localhost at port 3306
    - Results sorted in ascending order by cities.id
    - Displays in this manner: cities.id, cities.name, states.name
    - uses execute() once
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    argv = (sys.argv)[1:]
    db = MySQLdb.connect(user=argv[0], passwd=argv[1], db=argv[2])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                JOIN states ON states.id=cities.state_id
                ORDER BY cities.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
