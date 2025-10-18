""" 
LeagueBot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bot.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 
"""

import turtle as tina

screen = tina.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = tina.Turtle()

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = tina.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF


set_turtle_image(t, "leaguebot_bolt.gif")


t.shapesize(10, 10)


t.color('blue')

t.speed(0)

sides = 6
angle = 360/sides
size = 100

for i in range(sides):
    t.forward(size)                       # Move tina forward by the forward distance
    t.left(angle)        



tina.done()     