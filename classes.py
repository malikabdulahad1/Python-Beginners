class Point:
    x=10
    y=20
    z=90

    def move(self):
        print("move")


    def draw(self):
        print("draw")

point1= Point()
point1.draw()
point1.move()

print(point1.z)
point1.z=100
print(point1.z)




