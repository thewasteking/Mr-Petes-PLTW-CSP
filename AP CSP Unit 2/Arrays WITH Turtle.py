import turtle as t
wn = t.Screen()

objects = ["classic", "turtle", "arrow", "square", "triangle", "circle"]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x = 0
y = 0
for z in range(len(objects)):
    painter = t.Turtle()
    painter.shape(objects[z])
    painter.color(colors[z])
    x += 25
    painter.goto(x,y)

wn.mainloop()