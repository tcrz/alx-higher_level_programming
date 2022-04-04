#!/usr/bin/python3
"""
Class definition of City class.
(links to the MySQL table cities)
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    Defines City class links to the MySQL table cities
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")

