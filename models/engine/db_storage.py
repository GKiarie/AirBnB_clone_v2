#!/usr/bin/python3
'''DBStorage'''
from sqlalchemy import create_engine as ce, MetaData as md
from sqlalchemy.orm import sessionmaker as sm, scoped_session
from os import getenv as ge
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base, BaseModel


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = ge('HBNB_MYSQL_USER')
        pwrd = ge('HBNB_MYSQL_PWD')
        host = ge('HBNB_MYSQL_HOST')
        dtbs = ge('HBNB_MYSQL_DB')
        self.__engine = ce('mysql+mysqldb://{}:{}@{}/{}'.format(
                            user, pwrd, host, dtbs), pool_pre_ping=True)
        if ge('HBNB_ENV') == 'test':
            metadata = md()
            metadata.reflect(bind=self.__engine)
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        classes = [Amenity, State, City, Place, User, Review]
        Session = sm(bind=self.__engine)
        self.__session = Session()
        all_results = {}
        if cls and cls in classes:
            instances = self.__session.query(cls).all()
        else:
            instances = []
            for i in classes:
                instances.extend(self.__session.query(i).all())
        for obj in instances:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            all_results[key] = obj
        return all_results

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sm(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.close()
