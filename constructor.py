class Point:
    def __init__(self, x, y):
        self.x =x
        self.y=y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(20, 90)
print(point.x)
point.x=40
print(point.x)