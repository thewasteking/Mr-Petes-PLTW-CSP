import turtle as t
import random

wn = t.Screen()
wn.bgcolor("black")
painter = t.Turtle()

painter.shape("circle")
painter.speed(10)

painter.color("green")
painter.begin_fill()
for i in range(4):
    painter.forward(300)
    painter.right(90)
painter.end_fill()
   

painter.color("red")
painter.fillcolor("red")
painter.begin_fill()
painter.goto(0,0)
painter.goto(150,150)
painter.goto(300,0)
painter.end_fill()

painter.penup()
painter.goto(-150,150)
painter.color("white")
painter.begin_fill()
painter.pendown()
painter.circle(100)
painter.end_fill()

painter.penup()
painter.goto(210, -150)
painter.color("yellow")
painter.begin_fill()
painter.pendown()
for i in range(2):
    painter.forward(90)
    painter.right(90)
    painter.forward(90)
    painter.right(90)
painter.end_fill()

painter.penup()
painter.goto(0, -150)
painter.color("black")
painter.begin_fill()
painter.pendown()
for i in range(2):
    painter.forward(90)
    painter.right(90)
    painter.forward(90)
    painter.right(90)
painter.end_fill()

painter.penup()
painter.goto(110, -150)
painter.color("white")
painter.begin_fill()
painter.pendown()
for i in range(2):
    painter.forward(75)
    painter.right(90)
    painter.forward(150)
    painter.right(90)
painter.end_fill()

for i in range(50):
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    Size = random.randint(3,8)
    painter.penup()
    painter.goto(x,y)
    painter.pendown()

    painter.begin_fill()
    painter.circle(Size)
    painter.end_fill()

painter.hideturtle()

wn.mainloop()