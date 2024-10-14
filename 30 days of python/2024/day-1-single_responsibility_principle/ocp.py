from math import pi


class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type=='rectangle':
            self.width = kwargs["width"]
            self.height = kwargs['height']
        elif self.shape_type=='circle':
            self.radius = kwargs['radius']


    def calculate_are(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type=="circle":
            return pi * self.radius**2
        
#OCP

from abc import ABC, abstractmethod
from math import pi


class Shapr(ABC):
    def __init__(self,shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass
class Cirlcle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius
    def calcultae_area(self):
        return pi* self.radius**2
    
class Rectangle(Shape):
    def __init__(self, width,height):
        super().__init__("rectangle" )
        self.width = width
        self.height = height

    def calculate_are(self):
        return self.width * self.height
        
class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2