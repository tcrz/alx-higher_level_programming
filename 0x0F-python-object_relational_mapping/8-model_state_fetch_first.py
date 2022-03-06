#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa

    - script take 3 arguments: mysql username, mysql password and database name
    - uses the module SQLAlchemy
    - import State and Base from model_state
    - script connects to a MySQL server running on localhost at port 3306
    - The state you display must be the first in states.id
    - You are not allowed to fetch all states from the database
    before displaying the result
    - If the table states is empty, print 'Nothing' followed by a new line
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    s = Session()

    if not s.query(State).first():
        print("Nothing")
    else:
        row = (s.query(State).first())
        print('{}: {}'.format(row.id, row.name))
