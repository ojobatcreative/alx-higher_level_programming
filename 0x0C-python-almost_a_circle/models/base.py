#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Base model.

    This represents the foundational class for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_objects (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        self.id = id if id is not None else Base.__nb_objects + 1
        Base.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as jsonfile:
            list_dicts = [o.to_dictionary() for o in list_objs] if list_objs else []
            jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Deserializes a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        return json.loads(json_string) if json_string and json_string != "[]" else []

    @classmethod
    def create(cls, **dictionary):
        """Instantiates a class from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            new = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs:
                fieldnames = (
                    ["id", "width", "height", "x", "y"]
                    if cls.__name__ == "Rectangle"
                    else ["id", "size", "x", "y"]
                )
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
            else:
                csvfile.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = (
                    ["id", "width", "height", "x", "y"]
                    if cls.__name__ == "Rectangle"
                    else ["id", "size", "x", "y"]
                )
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        def draw_objects(objects, color):
            for obj in objects:
                turt.showturtle()
                turt.up()
                turt.goto(obj.x, obj.y)
                turt.down()
                for _ in range(2):
                    turt.forward(obj.width)
                    turt.left(90)
                    turt.forward(obj.height)
                    turt.left(90)
                turt.hideturtle()

        turt.color("#ffffff")
        draw_objects(list_rectangles, "#ffffff")

        turt.color("#b5e3d8")
        draw_objects(list_squares, "#b5e3d8")

        turtle.exitonclick()

