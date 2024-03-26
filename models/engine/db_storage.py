#!/usr/bin/python3
""" DBStorage engine setup"""

from sqlalchemy import create_engine, text, MetaData
from os import getenv
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:

    """DBStorage class"""


    __engine = None
    __session = None

    tables = {
            'State': State,
            'City': City,
            'User': User,
            'Place': Place,
            'Amenity': Amenity,
            'Review': Review
        }

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://' +
                                      f'{getenv("HBNB_MYSQL_USER")}:' +
                                      f'{getenv("HBNB_MYSQL_PWD")}@' +
                                      f'{getenv("HBNB_MYSQL_HOST")}:'
                                      f'3306/{getenv("HBNB_MYSQL_DB")}',
                                      pool_pre_ping=True)

        self.__session = Session()
        if getenv("HBNB_ENV") == 'test':
            metadata = MetaData(bind=self.__engine)
            metadata.reflect(bind=self.__engine)
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """returns the dictionary of records of the specific class"""
        my_dic = {}
        if cls is not None:
            result = self.__session.query(cls).all()
            for obj in result:
                my_dic[f"{obj.__class__.__name__}.{obj.id}] = obj
        else:
            for table in DBStorage.tables.values():
                result = self.__session.query(table).all()
                for obj in result:
                    my_dic[f"{obj.__class__.__name__}.{obj.id}] = obj
        return my_dic

    def new(self, obj):
        """ADD THE OBJECT TO THE CURRENT
            DATABASE SESSION"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to the database"""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from database"""

        self.__session.delete(obj)
        self.__session.commit()

    def reload(self):
        """Create all tables"""

        Session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
        Base.metadata.create_all(self.__engine)
