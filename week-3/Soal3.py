class Shape:
    width = 0
    def __init__(self, width):
        self.width = width
        
class Square (Shape):
    name = "Square"
    def get_area(self):
        return self.width ** 2
    
class Triangle (Shape):
    name = "Triangle"
    height = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
                
    def get_area (self):
        return 0.5 * self.width * self.height
    
SquareX = Square(5)
TriangleY = Triangle(width=5, height=3)

print(SquareX.get_area(), TriangleY.get_area())

