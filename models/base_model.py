#!/usr/bin/python3
"""This module contains the base model"""
import uuid
from datetime import datetime

class BaseModel:
    """Base class"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self):
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        return (f"[{self.__class__.__name__}]({self.id}){self.__dict__}")

    def save(self):
        self.update_at = datetime.now().isoformat()

    def to_dict(self):
        return self.__dict__
        
