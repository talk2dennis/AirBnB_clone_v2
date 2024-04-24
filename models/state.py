#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                           backref="state")


    if models.storage_name != "db":
        @property
        def cities(self):
            """ returns all the cities of a state """
            all_cities = []
            cities = models.storage.all(City)
            for city in cities:
                if city.state_id == self.id:
                    all_cities.append(city)
            return all_cities
