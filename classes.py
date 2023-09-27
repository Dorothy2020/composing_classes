# composing With Classes

class Point:
    def __init__(self, x, y):  # constructor method
        self.x = x
        self.y = y
class Shape:
    def __init__(self,points):
        self.points=points

triangle=Shape([point(0,0),
                Point(5,5),
                Point(2,4)])