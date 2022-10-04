#!/usr/bin/python3

"""Define class Base"""
import json


class Base:
    """Represents the base class

    Attr:
        __nb_objects: class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initilizing class base

        Args:
            id (int): a parameter value
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): list of dictionaries
        """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherits of Base
        """
        filename = "{}.json".format(cls.__name__)
        list_dict = []

        if list_objs is None:
            pass
        else:
            for ele in list_objs:
                if ele is not None:
                    list_dict.append(ele.to_dictionary())

        data_ser = Base.to_json_string(list_dict)

        with open(filename, 'w') as jsonfile:
            jsonfile.write(data_ser)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string representation into a list"""
        if (json_string is None or len(json_string) == 0):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if cls.__name__ == "Rectangle":
            new = cls(10, 5)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
