#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa

    - script takes 4 arguments: mysql username, mysql password, databasename
    and state name (SQL injection free!)
    - uses the module MySQLdb (import MySQLdb)
    - script connects to a MySQL server running on localhost at port 3306
    - Results are sorted in ascending order by cities.id
    - uses execute() once
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    argv = (sys.argv)[1:]
    db = MySQLdb.connect(user=argv[0], passwd=argv[1], db=argv[2])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities
                JOIN states ON states.id=cities.state_id
                WHERE states.name=%s
                ORDER BY cities.id ASC""", (argv[3],))
    rows = cur.fetchall()
    for row in rows:
        for col in row:
            if ((rows.index(row) + 1) is len(rows) and
               (row.index(col) + 1) is len(row)):
                print(col, end="")
            else:
                print(col, end=", ")
    print()
