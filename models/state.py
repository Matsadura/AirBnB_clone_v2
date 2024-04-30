#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="State",
                          cascade="all, delete-orphan")

    # Getter incase of storage type is FileStorage
    if getenv('HBNB_TYPE_STORAGE') == db:
        @property
        def cities(self):
            from models import storage
            """ getter method that returls list of City instances """
            return [City for Cities in storage.all("City").items()
                    if City.state_id == self.id]
