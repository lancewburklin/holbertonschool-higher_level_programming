#!/usr/bin/python3
"""
Start link class to table in database
"""


import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """ Yeah this does something """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).all()
    for row in result:
        if row.name == sys.argv[4]:
            print(row.id)
            sys.exit(0)
    print("Not found")
