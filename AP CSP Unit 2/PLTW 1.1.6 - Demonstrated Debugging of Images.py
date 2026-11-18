# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
# configure the spider's body
painter.pensize(40)
# draw the spider's head
painter.circle(20)
painter.penup()
painter.color("white")
painter.pensize(5)
painter.goto(-10,5)
painter.pendown()
painter.circle(1)
painter.penup()
painter.goto(10,5)
painter.pendown()
painter.circle(1)
painter.penup()
painter.color("black")
# configure the spider's legs
numberlegs = 8
leglength = 70
angle = (360 / numberlegs) - 20
painter.pensize(5)
n = 0
# draw the legs
while (n < numberlegs):
    painter.goto(0,20)
    painter.pendown()
    if n <= 3:
        painter.setheading(angle * n - 45)
    if n > 3:
        painter.setheading(angle * n + 45)
    painter.forward(leglength)
    n = n + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
