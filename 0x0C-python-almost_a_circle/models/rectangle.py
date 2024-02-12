#!/usr/bin/python3
""" Base Class """
import json
import os


class Base:
    """base class to manage id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initiation function of class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries and list_dictionaries != []:
            return json.dumps(list_dictionaries)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        instances_list = []
        if list_objs and list_objs != []:
            class_name = type(
                list_objs[0]
            ).__name__  #  or list_objs[0].__class__.__name__

            counter = 0
            obj_num = len(list_objs)
            dic_to_append = {}
            if class_name == "Rectangle":
                att = ["y", "x", "id", "width", "height"]
            elif class_name == "Sqaure":
                att = ["id", "size", "x", "y"]
            for i in range(obj_num):
                for att_name in att:
                    if att_name == "size":
                        dic_to_append[att_name] = getattr(list_objs[counter], "width")
                    dic_to_append[att_name] = getattr(list_objs[counter], att_name)
                instances_list.append(dic_to_append)
                # print(instances_list)
                counter += 1
                if counter == obj_num:
                    break
            # print(instances_list)
            with open("{}.json".format(class_name), "w") as file:
                file.write(Base.to_json_string(instances_list))
        else:
            return instances_list

    @staticmethod
    def from_json_string(json_string):
        if json_string and json_string != "":
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new_obj = Rectangle(1, 2)
        elif cls is Square:
            new_obj = Square(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new_obj = Rectangle(1, 2)
        elif cls is Square:
            new_obj = Square(1)
        instances_list = []
        class_name = cls
        if not os.path.exists(f"{class_name}.json"):
            return []
        else:
            with open(f"{class_name}.json", "r") as file:
                json_str = file.read()
            list_from_str = Base.from_json_string(json_str)
            for dic in list_from_str:
                instances_list.append(new_obj.update(dic))
            return instances_list


""" Class Rectangle """


class Rectangle(Base):
    """Class Rectangle that inherits base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initiation function of class"""

        for var_name, var_value in {"width": width, "height": height}.items():
            if type(var_value) is not int:
                raise TypeError(f"{var_name} must be an integer")

        for var_name, var_value in [("width", width), ("height", height)]:
            if var_value <= 0:
                raise ValueError(f"{var_name} must be > 0")

        for var_name, var_value in [("x", x), ("y", y)]:
            if var_value < 0:
                raise ValueError(f"{var_name} must be >= 0")

        # for var_name, var_value in {
        # 'width': width, 'height': height}.items():
        #     if var_value <= 0:
        #         raise ValueError(f"{var_name} must be > 0")

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for y_spaces in range(self.y):
            print()
        for i in range(self.height):
            for x_spaces in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        if args != ():  # empty tuple
            for arg, (var_name, var_value) in zip(args, self.__dict__.items()):
                setattr(self, var_name, arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        # method 1
        # return {
        #     'x': self.x,
        #     'y': self.y,
        #     'id': self.id,
        #     'height': self.height,
        #     'width': self.width,
        # } # { inidicate a dic }

        # method 2
        att = ["x", "y", "id", "height", "width"]
        representaion = {}
        for i in range(len(att)):
            if att[i] in self.__dir__():
                representaion[att[i]] = getattr(self, att[i])
                # print(representaion)
        return representaion
