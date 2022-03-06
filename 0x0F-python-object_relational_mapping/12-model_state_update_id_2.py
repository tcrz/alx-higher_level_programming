#!/usr/bin/python3
"""
script that changes the name of a State object from the database hbtn_0e_6_usa

    - script should take 3 arguments: mysql username,
    mysql password and database name
    - uses the module SQLAlchemy
    - import State and Base from model_state
    - script connecta to a MySQL server running on localhost at port 3306
    - Change the name of the State where id = 2 to New Mexico
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

#    state = s.merge(State(id=7))
    state = s.query(State).filter(State.id == 2).one()
    state.name = "New Mexico"
    s.commit()
