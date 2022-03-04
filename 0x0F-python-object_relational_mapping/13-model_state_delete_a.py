#!/usr/bin/python3
"""
script that deletes all State objects with a name containing the
letter 'a' from the database hbtn_0e_6_usa

    - script takes 3 arguments: mysql username, mysql password and databasename
    - uses the module SQLAlchemy
    - imports State and Base from model_state
    - script connects to a MySQL server running on localhost at port 3306
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

    for row in s.query(State).filter(State.name.contains('a'))\
                .order_by(State.id.asc()):
        s.delete(row)
    s.commit()
