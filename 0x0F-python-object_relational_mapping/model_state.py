#!/usr/bin/python3
"""Contains the class definition of a State and a Base instance"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Column, Integer, String

metaData = MetaData()
Base = declarative_base(metadata=metaData)


class State(Base):
    """Definition of the State class with id and name attributes"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
