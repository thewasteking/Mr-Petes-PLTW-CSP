import turtle as trtl
# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
tloc = 50
for s in turtle_shapes:
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions
for vt in vert_turtles:
  x1 = vt.xcor()
  y1 = vt.ycor()
  for ht in horiz_turtles:
    x2 = ht.xcor()
    y2 = ht.ycor()
    while y1 > -100 and x2 < 100:
      x2 += 5
      ht.goto(x2,y2)
      y1 -= 5
      vt.goto(x1,y1)
      if abs(y1- y2) <= 20:
        vt.shapesize(7)
        ht.shapesize(7)
        vt.shape("circle")
        ht.shape("circle")

wn = trtl.Screen()
wn.mainloop()