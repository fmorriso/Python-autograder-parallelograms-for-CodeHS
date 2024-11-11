# Here's another example of a class, this time
# with proper documentation throughout.
from math import sin


class Parallelogram:
    """
    This class represents a parallelogram.
    It has a side1 connected to a side2 and
    an angle between them. It is capable
    of computing its own area and perimeter.
    """

    def __init__(self, side1=0, side2=0, angle=0):
        """
        Initializes a parallelogram with optional
        side1, side2, and angle.
        """
        self.side1 = side1
        self.side2 = side2
        self.angle = angle

    def get_area(self) -> float:
        """return the area of the shape"""
        area = self.side1 * self.side2 * sin(self.angle)
        return area

    def get_perimeter(self) -> float:
        return 2.0 * (self.side1 + self.side2)

###################################
# Here's some example code that
# uses the Parallelogram class.

p1 = Parallelogram()
print(p1.side1)
print(p1.side2)
print(p1.angle)
print(f'{p1.get_area()=}')

p2 = Parallelogram(3, 4, 70)
print(p2.side1)
print(p2.side2)
print(p2.angle)
print(f'{p2.get_perimeter()=:.3f}')
print(f'{p2.get_area()=:.3f}')
