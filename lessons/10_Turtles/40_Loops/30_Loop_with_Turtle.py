"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

sides = 5
angle = 360/sides
size = 100

for i in range(sides):
    tina.forward(size)                       # Move tina forward by the forward distance
    tina.left(angle)        

turtle.exitonclick()