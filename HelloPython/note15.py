# class


class Point:
    # Constructors
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# point1 = Point()
# point1.move()
# point1.x = 10
# print(point1.x)

point2 = Point(10, 20)
print(point2.x)


# inheritance
class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    def sit(self):
        print('sit')


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()



