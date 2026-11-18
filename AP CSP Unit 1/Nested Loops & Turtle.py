import turtle as t
wn = t.Screen()

# Create a turtle
painter = t.Turtle()
# Create and modify the shape of the turtle
painter.shape("triangle")
# Lift the pen off the canvas
painter.penup()

x = -200
y = 100
painter.goto(x,y)

# create 6 rows and 5 columns of triangles
for r in range(6):
    painter.color("blue")
    painter.stamp()
    for c in range(5):
        x += 50
        painter.color("red")
        painter.goto(x,y)
        painter.stamp()
    x = -200
    y -= 50

wn.mainloop()