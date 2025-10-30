import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(500,500)
polygon = turtle.Turtle()
numsides = 6
sidelenght = 150
angle = 360/numsides
for i in range(numsides):
    polygon.forward(sidelenght)
    polygon.right(angle)
turtle.done()