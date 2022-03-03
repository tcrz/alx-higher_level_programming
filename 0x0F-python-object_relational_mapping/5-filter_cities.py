#!/usr/bin/python3
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
