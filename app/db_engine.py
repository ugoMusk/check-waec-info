#!/usr/bin/python3
"""
Creates records for the  waec_info database.
"""

from sys import argv
from center_data import Base, Center
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Acesess the database and writes to it.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    center_number = Center(centerNumber=cNumber) # cNumber not exit yet
    school_name = Center(schoolName=sName) # sName not exit yet
    town = Center(town=stown) # stown not exit yet

    session.add(cal_state)
    session.commit()
    session.close()
