from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def draw(self, drawer):
        pass


class Rectangle(Shape):

    def draw(self, drawer):
        print("Drawing rectangle  using : {}".format(drawer.name))


class Circle(Shape):

    def draw(self, drawer):
        print("Drawing circle using : {}".format(drawer.name))


class Triangle(Shape):

   def draw(self, drawer):
       print("Drawing triangle using : {}".format(drawer.name))

