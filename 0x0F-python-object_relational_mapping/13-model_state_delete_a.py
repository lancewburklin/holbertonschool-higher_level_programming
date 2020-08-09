#!/usr/bin/python3
"""
Start link class to table in database
"""


import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ Updates state with ID 2 """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    things = session.query(State).filter(State.name.like('%a%'))
    for stuff in things:
        if 'a' in stuff.name:
            session.delete(stuff)
    session.commit()
