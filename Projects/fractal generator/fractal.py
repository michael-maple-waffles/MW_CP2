#MW_CP2 fractal pattern

#import turtle
import turtle
import math

#make a triangle function:
def makeTriangle(position_x, position_y, distance, color, direction):
    #args will be distance of legs, where to place of the first leg, and if the triangle is upsidedown or rightside up
    
    #triangle = Turtle.turtle()
    triangle.penup()
    #triangle.setpos()
    triangle.setpos(position_x, position_y)
    triangle.pendown()
    triangle.fillcolor(color)
    #if triangle = 'ru':
    if direction == 'ru':
        triangle.begin_fill()
        #triangle.seth(0)
        triangle.seth(0)
        #triangl.forward(distance)
        triangle.forward(distance)
        #for i in range 1-2:
        for i in range(1,3):
            #triangle.left(120)
            triangle.seth(120*i)
            #triangle.forward(distance)
            triangle.forward(distance)
        triangle.end_fill()
    elif direction == 'ud':
        rounds = 0
        triangle.begin_fill()
        while rounds > 3:
            rounds += 1
            triangle.seth(60+120*rounds-1)
            triangle.forward(distance)
        triangle.end_fill()
        #triangle.forward(distance)
        
"""distance = 100
makeTriangle(0,0, distance, 'ru')
triangles = [(50,0,50)]
for i in range(3):
    for triangle in triangles:
        makeTriangle(triangle[0], triangle[1], triangle[2], 'ud')
        triangles.append(triangle[0]/2,triangle[1],triangle[2]/2)
        triangles.append(triangle[0]+triangle[0]/2,triangle[1],triangle[2]/2)
        triangles.append(triangle[0],(triangle[2]/2)*math.sqrt(3),triangle[2]/2)
        triangles.remove(triangle)"""

def getTriangle(side,x_cord,y_cord,dist):
    if side == 'L':
        new_x = x_cord/2
        new_dist = dist/2
        return(new_x, y_cord, new_dist)
    elif side == 'R':
        new_x = x_cord + x_cord/2
        new_dist = dist/2
        return(new_x, y_cord, new_dist)
    elif side == 'T':
        new_y = (dist/2)*math.sqrt(3)
        new_dist = dist/2
        return(x_cord, new_y, new_dist)



def fractalMaker(times, x_cord, y_cord, distance):
    colors = ['blue','red','green','white','yellow','violet','orange']
    print(f"{x_cord}, {y_cord}, {distance}")
    makeTriangle(x_cord, y_cord, distance, colors[times], 'ud')
    if times == 0:
        return 0
    else:
        fractalMaker(times = times-1, x_cord = getTriangle('L', x_cord, y_cord, distance)[0], y_cord=getTriangle('L', x_cord, y_cord, distance)[1], distance = getTriangle('L', x_cord, y_cord, distance)[2])

        fractalMaker(times = times-1, x_cord = getTriangle('R', x_cord, y_cord, distance)[0], y_cord=getTriangle('R', x_cord, y_cord, distance)[1], distance = getTriangle('R', x_cord, y_cord, distance)[2])

        fractalMaker(times = times-1, x_cord = getTriangle('T', x_cord, y_cord, distance)[0], y_cord=getTriangle('T', x_cord, y_cord, distance)[1], distance = getTriangle('T', x_cord, y_cord, distance)[2])



