import turtle as t
wn = t.Screen()

painter = t.Turtle()
painter.shape("triangle")
painter.forward(100)
painter.penup()
painter.goto(200,200)

painter.shape("square")
# Shapes = Classic, Circle, Square, Triangle, Arrow, Turtle
painter.color("red")
painter.pendown()
painter.circle(100)
painter.penup()

painter.goto(-200,200)
painter.pendown()
painter.circle(200,360)

painter.penup()
painter.goto(-200,-200)
painter.pendown()
painter.circle(100, steps=8)

painter.penup()
painter.goto(200,-200)
painter.pendown()
painter.circle(50,180)

painter.penup()
painter.goto(0,0)
painter.pendown()
for x in range(4):
    painter.forward(20)
    painter.right(90)
for y in range(18):
    painter.forward(20)
    painter.right(20)
for z in range(3):
    for a in range(3):
        painter.stamp()
        x += 10
    x = 0
    y = 0
wn.mainloop()