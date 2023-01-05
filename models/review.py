#!/usr/bin/python3
""" Review module for the HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        place_id = Column(String(60), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'),nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
