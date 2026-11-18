# #   a115_robot_maze.py
# import turtle as trtl

# #----- maze and turtle config variables
# screen_h = 400
# screen_w = 420
# startx = -100
# starty = -100
# turtle_scale = 1.5

# #------ robot commands
# def move():
#   robot.dot(10)
#   robot.fd(50)
# '''turns the robot left 
# '''
# def turn_left():
#   robot.speed(0)
#   robot.lt(90)
#   robot.speed(2)

# #----- init screen
# wn = trtl.Screen()
# wn.setup(width=screen_w, height=screen_h)
# robot_image = "robot.gif"
# wn.addshape(robot_image)

# #----- init robot
# robot = trtl.Turtle(shape=robot_image)
# robot.hideturtle()
# robot.color("darkorchid")
# robot.pencolor("darkorchid")
# robot.penup()
# robot.setheading(90)
# robot.turtlesize(turtle_scale, turtle_scale)
# robot.goto(startx, starty)
# robot.speed(2)
# robot.showturtle()

# #---- TODO: change maze here
# wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png

# #---- TODO: begin robot movement here
# # move robot forward with move()
# # turn robot left with turn_left()
# # sample for loop:

# # robot.right(90)

# # move()
  
# #---- end robot movement 

# wn.mainloop()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~THIS IS MAZE #1!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #   a115_robot_maze.py
# import turtle as trtl

# #----- maze and turtle config variables
# screen_h = 400
# screen_w = 420
# startx = -100
# starty = -100
# turtle_scale = 1.5

# #------ robot commands
# def move():
#   robot.dot(10)
#   robot.fd(50)
# '''turns the robot left 
# '''
# def turn_left():
#   robot.speed(0)
#   robot.lt(90)
#   robot.speed(2)
# def turn_right():
#     robot.speed(0)
#     robot.rt(90)
#     robot.speed(2)
  

# #----- init screen
# wn = trtl.Screen()
# wn.setup(width=screen_w, height=screen_h)
# robot_image = "robot.gif"
# wn.addshape(robot_image)

# #----- init robot
# robot = trtl.Turtle(shape=robot_image)
# robot.hideturtle()
# robot.color("darkorchid")
# robot.pencolor("darkorchid")
# robot.penup()
# robot.setheading(90)
# robot.turtlesize(turtle_scale, turtle_scale)
# robot.goto(startx, starty)
# robot.speed(2)
# robot.showturtle()

# #---- TODO: change maze here
# wn.bgpic("maze1.png") # other file names should be maze2.png, maze3.png

# #---- TODO: begin robot movement here
# # move robot forward with move()
# # turn robot left with turn_left()
# # sample for loop:

# i = 0
# # robot.right(90)
# for x in range(2):
#     for y in range(4):
#       move()
#     turn_right()

# # move()
# #---- end robot movement 

# wn.mainloop()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~THIS IS MAZE #2!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# #   a115_robot_maze.py
# import turtle as trtl

# #----- maze and turtle config variables
# screen_h = 400
# screen_w = 420
# startx = -100
# starty = -100
# turtle_scale = 1.5

# #------ robot commands
# def move():
#   robot.dot(10)
#   robot.fd(50)
# '''turns the robot left 
# '''
# def turn_left():
#   robot.speed(0)
#   robot.lt(90)
#   robot.speed(2)
# def turn_right():
#     robot.speed(0)
#     robot.rt(90)
#     robot.speed(2)
  

# #----- init screen
# wn = trtl.Screen()
# wn.setup(width=screen_w, height=screen_h)
# robot_image = "robot.gif"
# wn.addshape(robot_image)

# #----- init robot
# robot = trtl.Turtle(shape=robot_image)
# robot.hideturtle()
# robot.color("darkorchid")
# robot.pencolor("darkorchid")
# robot.penup()
# robot.setheading(90)
# robot.turtlesize(turtle_scale, turtle_scale)
# robot.goto(startx, starty)
# robot.speed(2)
# robot.showturtle()

# #---- TODO: change maze here
# wn.bgpic("maze2.png") # other file names should be maze2.png, maze3.png

# #---- TODO: begin robot movement here
# # move robot forward with move()
# # turn robot left with turn_left()
# # sample for loop:

# i = 0
# # robot.right(90)
# while i < 3:
#    move()
#    i += 1
# robot.right(90)

# i = 0
# while i < 2:
#    move()
#    i += 1

# robot.goto(startx, starty)

# for x in range(2):
#    for y in range(3):
#       move()
#    turn_left()

# move()
    

      
      

# # move()

# #---- end robot movement

# wn.mainloop()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~THIS IS MAZE #3!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)
'''turns the robot left 
'''
def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)
def turn_right():
    robot.speed(0)
    robot.rt(90)
    robot.speed(2)
  

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

#----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

#---- TODO: change maze here
wn.bgpic("maze3.png") # other file names should be maze2.png, maze3.png

#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample for loop:

i = 0
# robot.right(90)
for x in range(2):
   for y in range(2):
      move()
      robot.right(90)

      move()
      turn_left()
robot.color("#00FF00")
  
# move()

  
#---- end robot movement 

wn.mainloop()
