#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    results = session.query(State).order_by(State.id).first()
    print("Nothing" if not results else "{}: {}".format(results.id,
          results.name))
