from turtle import *
import math
#name your turtle
t= Turtle ()

#Set Up your screen and starting position
setup (500, 300)
### Write your code below:
sides = int(input ("Enter a number of sides that is greater than 2"))
color = str(input("what color?"))
def getInfo():
    sides2 = int(input ("Enter a number of sides that is greater than 2"))
    color = str(input("what color?"))
    t.shape(sides2)
    t.pencolor(color)
    return sides

def shape(sides):
    if (sides <= 2):
        print ("NO!!! pick a number greater than 2")
        sides = getInfo().sides2
    x = 360/sides
    if (sides >2):
        while sides > 2:
            t.forward(40)
            t.right (x)

shape(sides)
