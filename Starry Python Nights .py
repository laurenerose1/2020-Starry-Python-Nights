## This is a project where I create an image of a night sky using turtle and random libraries

from turtle import * #allows us to get graphic and functions for drawing - entire library
from random import randint #module/ library where we only plan on using one function to get a random integer for stars


setup(800, 500) #width and height in pixels
speed(0) #how fast we are drawing- 0 is as fast as possible
bgcolor("black") #background color for drawing

#create the moon in 2 parts 
# part one

penup()
goto(-300, 100)
pendown()
color("white")  #mooncolor
begin_fill()
circle(50)
end_fill()

#moon part 2- dark circle to make it more moon shape
penup()
goto(-280, 100)
pendown()
color("black")  #mooncolor
begin_fill()
circle(50)
end_fill()


#create a function to make basic star so we don't have to write it multiple times
def star():
    color("yellow") ## color of the star
    begin_fill()
    for i in range(5): #makes a 5 pointed star
        forward(10)
        right(144)
    end_fill()
    
#work on bulk star creation in random spaces
for i in range(40): #number of stars you want on screen
    x = randint(-500, 400) #left and right of page
    y = randint(-250, 250) #bottom and top of page
    star()
    penup() #lift our "pen" up so we can start doing new locations instead of being in one spot
    goto (x,y) #moves item to new coordinates for every loop
    pendown()


hideturtle()