#!/usr/bin/python3
"""
Custom base class for the entire project
"""

from uuid import uuid4
from datetime import datetime
import models
import models

class BaseModel:
    """Base class for all models in the AirBnb console project."""

    def __init__(self, *args, **kwargs):
        """Initialize public instance attributes."""
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(value, DATE_TIME_FORMAT)
                elif key == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Return string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update 'updated_at' with current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """Return a dictionary representation of the instance."""
        map_objects = {key: value.isoformat() if key in ("created_at", "updated_at") else value for key, value in self.__dict__.items()}
        map_objects["__class__"] = self.__class__.__name__
        return map_objects
