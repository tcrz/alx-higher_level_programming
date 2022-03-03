#!/usr/bin/python3
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
