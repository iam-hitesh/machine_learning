class Circle():
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return (self.radius ** 2)*Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r


circle1 = Circle(radius=3)
circle1.set_radius(100)

print(circle1.radius)
print(circle1.area())
