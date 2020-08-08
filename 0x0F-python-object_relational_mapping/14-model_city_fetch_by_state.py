#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ Gets all the states """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    for stt, cit in session.query(State, City).filter(
            State.id == City.state_id).all():
        print("{}: ({}) {}".format(stt.name, cit.id, cit.name))
