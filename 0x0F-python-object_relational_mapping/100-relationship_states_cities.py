#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    s = Session()

    new_state = State(name="California")
    new_state.cities = [
        City(name="San Francisco", state_id=1)
        ]
    s.add(new_state)
    s.commit()
