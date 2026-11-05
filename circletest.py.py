# this is my original code for drawing the circle
#import turtle
#import circle

#t = turtle.Turtle()

#circle.drawcircle(t, 0, 0, 100)

#turtle.done()
#this is where the ai helped me with the colors and spinning effect
# Imports the turtle library so we can draw and animate
import turtle

# Imports our circle.py file where the drawcircle function is stored
import circle

# Creates the turtle drawing window
screen = turtle.Screen()

# Sets the background color of the background to black for some reason it wanted the background black 
screen.bgcolor("black")

# Turns off automatic screen updates so the drawing doesn't flicker
screen.tracer(0)

# Creates a turtle object to draw the circle
t = turtle.Turtle()

# Sets the turtle speed to the fastest setting
t.speed(0)

# Hides the turtle arrow so only the circle is visible
t.hideturtle()

# Sets the starting rotation angle to 0 degrees
rotation = 0


# Defines the animation function
def animate():

    # Allows the function to change the rotation variable
    # that was created outside the function
    global rotation

    # Clears the previous drawing before drawing the next frame
    t.clear()

    # Calls the drawcircle function from circle.py
    # Draws a circle centered at (0, 0) with a radius of 100
    # Uses the current rotation angle
    circle.drawcircle(t, 0, 0, 100, rotation)

    # Updates the screen to display the completed drawing
    screen.update()

    # Increases the rotation by 3 degrees each time
    # The % 360 keeps the angle between 0 and 359 degrees
    rotation = (rotation + 3) % 360

    # Calls the animate function again after 500 milliseconds
    # This makes the circle continue rotating
    screen.ontimer(animate, 500)


# Starts the animation for the first time
animate()

# Keeps the turtle window open and running
screen.mainloop()
