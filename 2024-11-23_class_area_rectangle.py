class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

# Creating a rectangle object
rectangle = Rectangle(5, 5)
print(f"Area of Rectangle: {rectangle.calculate_area()}")
