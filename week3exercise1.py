from abc import ABC, abstractmethod
import math

class Shape3D(ABC):
    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def surface_area(self):
        pass

    def describe(self):
        return "This is a 3D shape."

class Cube(Shape3D):
    def __init__(self, side):
        self.side = side

    def volume(self):
        return self.side ** 3

    def surface_area(self):
        return 6 * (self.side ** 2)

class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    def surface_area(self):
        return 4 * math.pi * (self.radius ** 2)

class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))

my_cube = Cube(2)
my_sphere = Sphere(3)
my_cylinder = Cylinder(2, 5)

shapes = [my_cube, my_sphere, my_cylinder]

for shape in shapes:
    print(f"--- {type(shape).__name__} ---")
    print(shape.describe())
    print(f"Volume: {shape.volume():.2f}")
    print(f"Surface Area: {shape.surface_area():.2f}")
    print()