
# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()

sides = 5
angle = 360/sides
size = 100

for i in range(sides):
    tina.forward(size)
    tina.left(angle)

turtle.exitonclick()                    # Close the window when we click on it