#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}


if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    from engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()