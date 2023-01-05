#!/usr/bin/python3
"""define class to instantiate engine"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class DBStorage:


    """
    Private attr:
        __engine:None
        __Session: None
    Public instance methods:
        __init__(self):
            self.__engine: create the engine
            linked to db (hbnb_dev and hbnb_dev_db) created before
            dialect: mysql
            driver: mysqldb
        .env variables 
            MySQL user: HBNB_MYSQL_USER
            MySQL password: HBNB_MYSQL_PWD
            MySQL host: HBNB_MYSQL_HOST (here = localhost)
            MySQL database: HBNB_MYSQL_D
        
    """
    __engine = None
    __session = None

    def __init__(self):
        """initialize the obj"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                        format(getenv("HBNB_MYSQL_USER"),
                                        getenv("HBNB_MYSQL_PWD"),
                                        getenv("HBNB_MYSQL_HOS"),
                                        getenv("HBNB_MYSQL_DB"),
                                        pool_pre_ping=True))
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        dictionary = {}
        if cls == None:
            obj = [User, State, City, Amenity, Place, Review]
            for classes in obj:
                query = self.__session.query(classes)
                for qry in query:
                    key = '{}.{}'.format(qry.__class__.__name__, qry.id)
                    dictionary[key] = qry
        else:
            obj = self.__session.query(cls).all()
            for v in obj:
                key = v.__class__.__name__ + '.' + v.id
                dictionary[key] = v
        return dictionary
    
    def new(self, obj):
        """ add the obj to the current db session"""
        self.__session.add(obj)
    
    def save(self):
        """commit all changes of the current db session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """delete from the current db session if obj != None"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """
        create all tables in the db
        """
        self.__session = Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()