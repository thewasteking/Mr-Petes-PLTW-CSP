import turtle as t
wn = t.Screen()
painter1 = t.Turtle()
painter2 = t.Turtle()

painter1.shape("turtle")
painter2.shape("turtle")
painter1.penup()
painter2.penup()
painter2.setheading(-180)
x1 = -200
x2 = 200
y1 = 0
y2 = 0
painter1.goto(x1,y1)
painter2.goto(x2,y2)

while x1 < 300 and x2 > -300:
    painter1.forward(5)
    painter2.forward(5)
    if abs(painter1.xcor()-painter2.xcor() and abs(painter1.ycor()-painter2.ycor())) <= 20:
        painter1.color("red")
        painter2.color("blue")
        painter1.setheading(90)
        painter2.setheading(-90)

wn.mainloop()