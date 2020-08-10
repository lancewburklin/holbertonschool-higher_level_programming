#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ Gets all the states """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State()
    new_state.name = "California"
    new_city = City()
    new_city.name = "San Francisco"
    new_state.cities = [new_city]
    session.add(new_state)
    session.commit()
    session.close()
