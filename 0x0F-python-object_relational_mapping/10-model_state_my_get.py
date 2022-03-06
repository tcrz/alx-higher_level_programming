#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa

    - script should take 4 arguments: mysql username, mysql password,
    database name and state name to search (SQL injection free)
    - uses the module SQLAlchemy
    - imports State and Base from model_state
    - script connects to a MySQL server running on localhost at port 3306
    - You can assume you have one record with the state name to search
    - Results must display the states.id
    - If no state has the name you searched for, display Not found
"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine, not_, text
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    s = Session()

    row = s.query(State).filter(State.name == sys.argv[4]).first()
    if row:
        print(row.id)
    else:
        print("Not found")
