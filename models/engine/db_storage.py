#!/usr/bin/python3
""" A module that contains the class engine DBStorage """
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session

# Getting the value of the enviromental variables
user = getenv('HBNB_MYSQL_USER')
passwd = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
hbnb_env = getenv('HBNB_ENV')

# Preparing the engine URL
url = f"mysql+mysqldb://{user}:{passwd}@{host}:3306/{db}"


class DBStorage():
    """ A Database engine class """
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of attributes """
        self.__engine = create_engine(url, pool_pre_ping=True)

        # TO DO : Drop All tables if env_var HBNB_ENV equals "test"

    # TO DO
    def all(self, cls=None):
        """ Return the query of all objects """
        pass

    def new(self, obj):
        """ Adds the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables and thecurrent database session """
        # TO DO : Create all tables in the database

        # Creating the current database session
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        self.__session = scoped_session(self.__session)


