#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from os import environ
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy Base class declaration
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    # id, created_at, updated_at SQLAlchemy class attributes
    __abstract__ = True
    id = Column(String(60), primary_key=True, unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
    
    def __str__(self):
        """Returns a string representation of the instance"""
        new_dict = self.__dict__
        try:
            del (new_dict["_sa_instance_state"])
        except KeyError:
            pass
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, new_dict)

    def __repr__(self):
        """Returns a string representation of the instance"""
        new_dict = self.__dict__
        try:
            del (new_dict["_sa_instance_state"])
        except KeyError:
            pass
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, new_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()

        # The moved storage.new(self) from __init__
        storage.new(self)

        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        # Remove _sa_instance_state only if this key exists
        try:
            del(dictionary['_sa_instance_state'])
        except:
            pass
        return dictionary

    # delete the current instance from the storage
    def delete(self):
        """ Delete the current instance from storage """
        from models import storage
        storage.delete(self)
