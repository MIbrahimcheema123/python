import turtle
turtle.Screen().bgcolor("brown")
turtle.Screen().title("spiral")
pen = turtle.Turtle()
pen.color("yellow")
size = 0
while True:
    for i in range(4):
        pen.fd(size+1)
        pen.left(90)
        size -= 5
    size += 1