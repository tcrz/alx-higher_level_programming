#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa:
    - script takes 3 arguments: mysql username, mysql password
    and database name (no argument validation needed)
    - use the module MySQLdb (import MySQLdb)
    - script connects to a MySQL server running on localhost at port 3306
    - Results are sorted in ascending order by states.id
"""

if __name__ == '__main__':
    import MySQLdb

    db = MySQLdb.connect(user="root", passwd="crzctrl",  db="hbtn_0e_0_usa")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for i in rows:
        print(i)
