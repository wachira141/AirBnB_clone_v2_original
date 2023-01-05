#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls != None:
            temp = {}
            for k, v in FileStorage.__objects.items():
                if k.split('.')[0] == cls:
                    temp[k] = v
            return temp
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj}) 
        """use of __class__ is to access class created dynamically"""
    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f) 

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place 
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        print('{}: {}'.format(key, val))
                        self.all()[key] = classes[val['__class__']](**val)
                        # print(classes[val['__class__']](**val))
        except FileNotFoundError:
            pass
    
    def delete(self, obj=None):
        """Deletes obj from __objects"""
        for k, v in FileStorage.__objects.items():
            if v is obj:
                del FileStorage.__objects[k]
                self.save()
                break

