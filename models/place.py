#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String,Float,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
import models
from models import amenity

# if os.getenv("HBNB_TYPE_STORAGE") == 'db':

place_amenity = Table('place_amenity', Base.metadata,
                        Column('place_id', String(60),
                                ForeignKey('places.id'),
                                primary_key=True,
                                nullable=False),
                        Column('amenity_id', String(60),
                                ForeignKey('amenities.id'),
                                primary_key=True,
                                nullable=False)
                        )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'),nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'),nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place', cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
            Return a list of Review instances with 
            place_id == Place.id from
            FileStorage
            """
            from models import review
            from models import storage
            review_list = []
            for review in storage.all(review.Review).values():
                if review.place._id == self.id:
                    review_list.append(review)
            return review_list 

        @property
        def amenities(self):
            """
            return the list of Amenity inst based on the
            the attr amenity_ids that contains Amenity.id
            """
            list_amenities = []
            
            for amn in models.storage.all(amenity.Amenity).values():
                if amn.place_id == self.id:
                    list_amenities.append(amn)
            return list_amenities

        @amenities.setter
        def amenities(self, obj):
            """
            that handles append method for adding an
            Amenity.id to the attribute amenity_ids
            """
            if obj != None:
                from models import storage
                
                for objs in storage.all(amenity.Amenity).values():
                    if objs.place_id == self.id:
                        self.amenity_ids.append(objs)
            


   
