#!/usr/bin/python3
"""Base Class Definition"""
import json
import csv


class Base:
    """The base class that manages the id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Assigns the id of an instance

            Args:
                id: ID of an instance
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of a list of dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            str_json = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                    )
            f.write(str_json)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of dictionaries from the JSON string rep."""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all its attributes already set"""
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        elif cls.__name__ == "Square":
            temp = cls(1)
        else:
            raise ValueError("Unsupported class type")

        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                str_json = f.read()
                list_dict = cls.from_json_string(str_json)
                return [cls.create(**dictionary) for dictionary in list_dict]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialized ;list_objs to a CSV file"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from CSV file"""
        filename = cls.__name__ + ".csv"
        objs = []
        try:
            with open(filename, "r", newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        id, width, height, x, y, = map(int, row)
                        obj = cls(width, height, x, y, id)
                    elif cls.__name__ == "Square":
                        id, size, x, y = map(int, row)
                        obj = cls(size, x, y, id)
                    objs.append(obj)
        except FileNotFoundError:
            pass
        return objs
