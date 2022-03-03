#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(user="root", passwd="crzctrl", db="hbtn_0e_0_usa")
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
rows = cur.fetchall()
for r in rows:
    print(r)
