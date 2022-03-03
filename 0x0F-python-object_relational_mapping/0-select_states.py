#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(user="root", passwd="crzctrl",  db="hbtn_0e_0_usa")
cur = db.cursor()
cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for i in rows:
    print(i)
