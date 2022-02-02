#!/bin/python3
"""Base model for air bnb clone"""
import uuid
from datetime import datetime
from models.__init__ import storage


class BaseModel():
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        self.created_at = datetime.fromisoformat(value)
                    elif key == "updated_at":
                        self.updated_at = datetime.fromisoformat(value)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format("BaseModel", self.id, self.__dict__)

    def save(self):
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__["__class__"] = "BaseModel"
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return(self.__dict__)