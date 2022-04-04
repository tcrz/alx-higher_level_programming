#!/usr/bin/python3
"""
Class definition of State class.
(links to the MySQL table states)
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    Defines State class links to the MySQL table states
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")
