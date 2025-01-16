#!/usr/bin/python3
from models.base_model import BaseModel
from json import dump, load
from os import path

class FileStorage:

    __file_path = "./file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        dict_to_json = {}
        for key, value in FileStorage.__objects.items():
            dict_to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding='utf-8') as file:
            dump(dict_to_json, file)

    def reload(self):
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding='utf-8') as file:
                dict_from_json = load(file)
            for key, value in dict_from_json.items():
                class_name = value["__class__"]
                del value["__class__"]
                self.new(eval(class_name)(**value))
        else:
            pass