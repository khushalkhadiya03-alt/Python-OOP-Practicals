
import math

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        d = math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
        return d

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


# Taking input from the user
x1 = float(input("Enter x coordinate of first point: "))
y1 = float(input("Enter y coordinate of first point: "))

x2 = float(input("Enter x coordinate of second point: "))
y2 = float(input("Enter y coordinate of second point: "))

# Creating point objects
p1 = Point2D(x1, y1)
p2 = Point2D(x2, y2)

# Displaying points
print("First point:", p1)
print("Second point:", p2)

# Calculating distance
print("Distance between points:", p1.distance(p2))
