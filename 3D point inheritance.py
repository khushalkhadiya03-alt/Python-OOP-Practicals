
import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 +
                         (self.y - p.y)**2)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    # Overriding distance method
    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 +
                         (self.y - p.y)**2 +
                         (self.z - p.z)**2)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"


# Taking input from the user
x1 = float(input("Enter x coordinate of first point: "))
y1 = float(input("Enter y coordinate of first point: "))
z1 = float(input("Enter z coordinate of first point: "))

x2 = float(input("Enter x coordinate of second point: "))
y2 = float(input("Enter y coordinate of second point: "))
z2 = float(input("Enter z coordinate of second point: "))

# Creating objects
p1 = Point3D(x1, y1, z1)
p2 = Point3D(x2, y2, z2)

# Displaying points
print("First point:", p1)
print("Second point:", p2)

# Calculating distance
print("Distance between points:", p1.distance(p2))
