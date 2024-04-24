#!/usr/bin/python3
""" new class for sqlAlchemy Database """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create all the tables"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        returns all the datas in the database
        """

        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            datas = self.__session.query(cls)
            for data in datas:
                key = f"{type(data).__name__}.{data.id}"
                dic[key] = data
        else:
            lists = [State, City]#, User, Place, Review, Amenity]
            for obj in lists:
                datas = self.__session.query(obj)
                for data in datas:
                    key = f"{type(data).__name__}.{data.id}"
                    dic[key] = data
        return (dic)

    def new(self, obj):
        """adds a data to the table
        """
        self.__session.add(obj)

    def save(self):
        """saves changes made and commits them
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete a data from the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """Reloads the configurations
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ closes the sessions
        """
        self.__session.remove()
