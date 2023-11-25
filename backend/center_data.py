#!/usr/bin/python3
"""
Define data for center_data table on mysql database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Center(Base):
    """State class

    Attributes:
        __tablename__ (str): database table name
        centerNumber (int): holds values for school center numbers 
        schoolName (str): holds values for name of school
        town (str): holds values for town where school is situated
    """
    __tablename__ = 'center_data'

    centerNumber = Column(Integer, primary_key=True)
    schoolName = Column(String(128), nullable=False)
    town = Column(String(128), nullable=False)
