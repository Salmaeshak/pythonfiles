from abc import ABC
class Polygon(ABC):
    def sides(self):
        pass
    def display(self):
        print("the polygon")
class triangle(Polygon):
    def sides(self):
        print("the triangle has 3 sides")
t = triangle()
t.display()
t.sides()

