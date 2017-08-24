from turtle import *
import math
#name your turtle
t= Turtle ()
sides = int(input ("Enter a number of sides that is greater than 3."))
color = input("what color?")
t.pencolor(color)
x = 360/sides
n = sides
#Set Up your screen and starting position
setup (500, 300)
### Write your code below:

while sides > 2:
    for repeats in range(n):
        t.forward(40)
        t.right (x)
if sides <= 2:
     print ("NO!!! pick a number greater than 2")




# Close window on click.
exitonclick ()
