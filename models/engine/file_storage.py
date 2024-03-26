#!/usr/bin/python3
"""File storage"""
import json


class FileStorage:
    """This class converts object to json and save"""
    __file_path = "file.json"
    __objects = {}


    def all(self):
        return self.__objects

    def new(self, obj):
        if obj is not None:
            key = obj.__class__.__name__+'.'+obj.id
            self.__objects[key] = obj
    
    def save(self):
        with open(self.__file_path, "w") as outfile:
            json.dump(self.__objects, outfile)

    def reload(self):
        try:
            with open(self.__file_path, "r") as inputfile:
               input_jason =  json.load(inpufile)
        except:
            pass




