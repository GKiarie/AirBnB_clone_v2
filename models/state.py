#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv as ge
from models.city import City


class State(BaseModel, Base):
    """ State class
    name = ""
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if ge("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            '''getter method, returns list of city objects from storage'''
            from models import storage
            cities_dict = storage.all(City)
            city_list = []
            for city in cities_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list