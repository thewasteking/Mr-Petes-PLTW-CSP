import turtle as t

wn = t.Screen()

painter = t.Turtle()

painter.shape("classic")
painter.setheading(0)
painter.color("purple")
painter.forward(100)
painter.right(90)
painter.color("red")
painter.forward(100)
painter.right(90)
painter.color("orange")
painter.forward(100)
painter.right(90)
painter.color("blue")
painter.forward(100)
painter.right(90)
painter.color("pink")

painter.penup()
painter.goto(50,50)
painter.pendown()
for i in range(4):
    painter.color("yellow")
    painter.forward(100)
    painter.right(90)

painter.penup()
painter.goto(100,100)
painter.pendown()
for i in range(4):
    painter.color("green")
    painter.forward(100)
    painter.right(90)

painter.penup()
painter.goto(150,150)
painter.pendown()
for i in range(4):
    painter.color("black")
    painter.forward(100)
    painter.right(90)

painter.goto(200,200)
painter.stamp()
painter.goto(0,0)
painter.hideturtle()

painter.goto(0,200)
painter.goto(200,200)

wn.mainloop()