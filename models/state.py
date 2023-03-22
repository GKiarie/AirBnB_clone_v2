#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class State(BaseModel, Base):
    """ State class
    name = ""
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
