#!/usr/bin/python3
""" Base Class """


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
        return f"[Rectangle] (
            {self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        if args and args != ():  # empty tuple
            for arg, (var_name, var_value) in zip(args, self.__dict__.items()):
                setattr(self, var_name, arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


class Square(Rectangle):
    """Class Sqaure the Inherts Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value  # super(),.width(value)
        self.height = value

    def update(self, *args, **kwargs):
        if args and args != ():
            attributes = ["id", "size", "x", "y"]
            counter = 0
            for arg in args:
                if counter == 1:
                    self.width = arg
                    self.height = arg
                    counter += 1
                    # print(attributes[counter])
                    # print(" updtaed siize counter now is {}".format(counter))
                else:
                    # print(attributes[counter])
                    setattr(self, attributes[counter], arg)
                    counter += 1
                    # print(" updtaed att counter now is {}".format(counter))
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                    self.height = value
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        # method 1
        # return {
        #     'x': self.x,
        #     'y': self.y,
        #     'id': self.id,
        #     'size': self.height
        # } # { inidicate a dic

        # method 2
        att = ["id", "size", "x", "y"]
        representaion = {}
        for i in range(len(att)):
            if i == 1:
                representaion[att[i]] = getattr(self, "width")
            else:
                if att[i] in self.__dir__():
                    representaion[att[i]] = getattr(self, att[i])
        return representaion
