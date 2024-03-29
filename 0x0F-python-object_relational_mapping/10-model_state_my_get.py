#!/usr/bin/python3
"""prints the State object with the name passed as argument from the
database hbtn_0e_6_usa
If no state has the name you searched for, display Not found
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
    name = sys.argv[4]
    results = session.query(State).filter(State.name == sys.argv[4]).first()
    print("Not found" if not results else results.id)
