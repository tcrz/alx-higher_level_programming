#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

    - script takes 3 arguments: mysql username, mysql password and databasename
    - uses the module SQLAlchemy
    - imports State and Base from model_state
    - script should connect to a MySQL server running on localhost at port 3306
    Print the new states.id after creation
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

    new_state = State(name="Louisiana")
    s.add(new_state)
    s.commit()
    print(new_state.id)
