#MW_CP2 fractal generator.main

from fractal import makeTriangle, fractalMaker
import turtle

def main():
    triangle = turtle.Turtle()
    triangle.hideturtle()
    triangle.speed(0)
    screen = turtle.Screen()
    makeTriangle(0,0,500,'white','ru')
    fractalMaker(5,250,0,250)
    screen.exitonclick()
