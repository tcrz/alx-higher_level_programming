#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa

Your script should take 3 arguments: mysql username, mysqlpassword
and database name
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost at port 3306
You must use only one query to the database
You must use the state relationship to access to the State object
linked to the City object
Results must be sorted in ascending order by cities.id
"""

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

    for row in s.query(City).order_by(City.id.asc()):
        print('{}: {} -> {}'.format(row.id, row.name, row.state.name))
