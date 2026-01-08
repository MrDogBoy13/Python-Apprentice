"""
Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(0)                           # Make the turtle move as fast, but not too fast. 

forwards = [80,1,67,96, 10, 10, 20, 30, 14, 34]
lefts = [91, 227, 3.67, 21.5, 4.86, 90.3456, 10, 1, 21, 1]
colors = ["red", "blue", "green", "purple","red", "blue", "green", "purple", "red", "blue", "green", "orange"]

for t in range(360):
    for  i in range(10):

        forward = forwards[i]
        left = lefts[i]
        color = colors[i]

        tina.color(color)
        tina.forward(forward)
        tina.left(left)

turtle.exitonclick()  