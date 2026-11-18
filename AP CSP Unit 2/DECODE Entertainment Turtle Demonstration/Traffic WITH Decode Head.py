import turtle as t
wn = t.Screen()
painter1 = t.Turtle()
painter2 = t.Turtle()

image_file = "2007 DECODE Head.gif"
wn.register_shape(image_file)
painter1.shape(image_file)
painter2.shape(image_file)
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
    if abs(painter1.xcor()-painter2.xcor()) <= 20:
        painter1.setheading(90)
        painter2.setheading(-90)

wn.mainloop()
