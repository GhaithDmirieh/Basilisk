import turtle
import random
from turtle import RawTurtle, TurtleScreen

class Object:
    """Die Klasse Beschreibt wie ein Obst oder Gift aussieht"""

    def __init__(self, window, shape):
        self.obj = RawTurtle(window)
        self.obj.speed(0)
        self.obj.shape(shape)
        self.obj.penup()
        self.obj.goto(0,100)

    def getObj(self):
        return self.obj
    
    def getYPos(self):
        return self.obj.ycor()

    def getXPos(self):
        return self.obj.xcor()

    # In Dieser Methode wird ein Obst oder ein Gift genau auf die Stelle gesetzt, an der der Schlangenkopf es genau im richtige Pixel treffen kann.
    def setPos(self, x, y):
        self.obj.goto(x,y)
        self.obj.sety(self.obj.ycor()-(self.obj.ycor()%20))
        self.obj.setx(self.obj.xcor()-(self.obj.xcor()%20))
        return
    
    def hideObj(self):
        self.obj.hideturtle()
    
    def randomPos(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.setPos(x, y)