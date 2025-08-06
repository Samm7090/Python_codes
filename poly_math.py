import math

class shape:
    def area(self):
        return 0
    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius ** 2
    
class rectangle(shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def area(self):
        return self.height*self.width
    


shapes=[circle(5),rectangle(4,6)]

for shape in shapes:
    print(f"Area is : {shape.area():.2f}") 