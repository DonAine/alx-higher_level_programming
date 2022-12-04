#!/usr/bin/python3

'''
class city

'''

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    i """Represents a city for a MySQL database.
        Attributes:
                    id (Integer): The city's id.
                    name (sqlalchemy.String): The city's name.
                    state_id (sqlalchemy.Integer): The city's state id.
      """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
