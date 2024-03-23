#!/usr/bin/python3
"""This module contains the base model"""
import uuid
from datetime import datetime


time_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if self.created_at and type(self.created_at) is str:
                self.created_at = datetime.strptime(self.created_at, time_format)
            else:
                self.created_at = datetime.utcnow()
            if self.updated_at and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(self.updated_at, time_format)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id") is None:
                self.id = str(uuid.uuid4())
        else:
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            self.id = str(uuid.uuid4())

    def __str__(self):
        return (f"[{self.__class__.__name__}]({self.id}){self.__dict__}")

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        classdict = self.__dict__
        classdict["__class__"] = self.__class__.__name__
        return (classdict)
