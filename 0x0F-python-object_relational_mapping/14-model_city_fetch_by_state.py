#!/usr/bin/python3
"""
script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa:

    - script takes 3 arguments: mysql username, mysql password and database ame
    - use the module SQLAlchemy
    - must import State and Base from model_state
    - script connects to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - Results must be display this way: (<state name>: (<city id>) <city name>)
"""


if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    s = Session()

    for state, city in s.query(State, City).filter(State.id == City.state_id)\
                        .order_by(City.id.asc()):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
