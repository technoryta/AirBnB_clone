#!/usr/bin/python3
"""This module contains the base model"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class"""

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())

    def __str__(self):
        return (f"[{self.__class__.__name__}]({self.id}){self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        classdict = self.__dict__
        classdict["__class__"] = self.__class__.__name__
        return (classdict)
