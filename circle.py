#Leo Esparza
#CIT-104-A.26AU
#Prof.Giles
#11/5/2026
#this is my original code for the circle
#import math

#def drawcircle(t, x, y, radius):
 #   circumference = 2.0 * math.pi * radius
  #  distance = circumference / 120.0

    #t.goto(x, y - radius)

    #for count in range(120):
     #   t.forward(distance)
      #  t.left(3)

    #I had ai help with the spinning circle and we came up with some slight changes for this and the other file
    #this is the prompt i used i gave it my codes then said  Fill each of the 120 sectors with a random color. or make a pattern of your choosing. Make the colors rotate. Make the pattern you
    # used rotate around the circle in a 60 second time frame i need it to fill the colors then hold that picture of the circle filled with the colors then spin around taking 60 seconds to do a full rotation
    # it wanted me to install pillow so i just asked if i could do it without installing anything and it gave me this 

import math
import random

# Creates an empty list to store the 120 random colors
colors = []

# Repeats 120 times to create 120 different random colors
for count in range(120):

    # Creates a random color using red, green, and blue values
    # Each value is between 0 and 1
    colors.append((random.random(), random.random(), random.random()))


# Defines the function to draw the circle
# t = turtle object
# x = x coordinate of the center
# y = y coordinate of the center
# radius = size of the circle
# rotation = angle used to rotate the colors
def drawcircle(t, x, y, radius, rotation):

    # Calculates the distance for each of the 120 sections
    distance = (2.0 * math.pi * radius) / 120.0

    # Repeats the process 120 times to create the circle
    for count in range(120):

        # Converts the section's angle from degrees to radians
        # Adds rotation so the colors can move around the circle
        angle = math.radians(count * 3 + rotation)

        # Calculates the x coordinate of the first outside point
        x1 = x + radius * math.cos(angle)

        # Calculates the y coordinate of the first outside point
        y1 = y + radius * math.sin(angle)

        # Calculates the x coordinate of the next outside point
        x2 = x + radius * math.cos(angle + math.radians(3))

        # Calculates the y coordinate of the next outside point
        y2 = y + radius * math.sin(angle + math.radians(3))

        # Lifts the turtle pen so it doesn't draw while moving
        t.penup()

        # Moves the turtle to the center of the circle
        t.goto(x, y)

        # Selects the random color for this section
        t.fillcolor(colors[count])

        # Starts filling in the section with color
        t.begin_fill()

        # Puts the pen down so the turtle can draw
        t.pendown()

        # Draws a line from the center to the first outside point
        t.goto(x1, y1)

        # Draws a line to the next outside point
        t.goto(x2, y2)

        # Returns to the center to complete the section
        t.goto(x, y)

        # Fills the completed section with its selected color
        t.end_fill()