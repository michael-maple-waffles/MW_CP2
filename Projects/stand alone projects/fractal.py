#MW_CP2 fractal pattern

#import turtle
import turtle

"""#make a triangle function:
def makeTriangle(position_x, position_y, distance, direction):
    #args will be distance of legs, where to place of the first leg, and if the triangle is upsidedown or rightside up

    #triangle = Turtle.turtle()
    triangle = turtle.Turtle()
    triangle.hideturtle()
    triangle.penup()
    #triangle.setpos()
    triangle.setpos(position_x, position_y)
    triangle.pendown
    #if triangle = 'ru':
    if direction == 'ru':
        #triangle.seth(0)
        triangle.seth(0)
        #triangl.forward(distance)
        triangle.forward(distance)
        #for i in range 1-2:
        for i in range(1,3):
            #triangle.left(120)
            triangle.left(120)
            #triangle.forward(distance)
            triangle.forward(distance)
    elif direction == 'ud':
        triangle.seth(0)
        #triangl.forward(distance)
        triangle.forward(distance)
        #for i in range 1-2:
        for i in range(1,3):
            #triangle.left(120)
            triangle.right(120)
            #triangle.forward(distance)
            triangle.forward(distance)

makeTriangle(0,0, 100, 'ru')
makeTriangle(50,50,50,'ud')"""

#make triangle:
def makeTriangle(distance):
    #forward by distance, right 120 degrees
    triangle = turtle.Turtle()
    triangle.hideturtle()
    for i in range(3):
        triangle.forward(distance = distance)
        triangle.left(120)

def fractalMaker(times, distance):
    if times == 0:
        return distance
    elif times >= 0:
        
