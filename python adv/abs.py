from abc import ABC,abstractmethod
class polygon(ABC):
    @abstractmethod
    def no_of_sides(self):
        pass
class triangle(polygon):
    def __init__(self):
        pass
    def no_of_sides(self):
        print("i have 3 sides")
class rectangle(polygon):
    def __init__(self):
        pass
    def no_of_sides(self):
        print("i have 4 sides")

obj1 =triangle()
obj2=rectangle()
obj1.no_of_sides()
obj2.no_of_sides()