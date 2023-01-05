#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state',
                                cascade='all, delete, delete-orphan')
    else:
        name=""

        @property
        def cities(self):
            cities = []
            from models import storage
            from models.city import City
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
