import turtle
import random

class Object:
    def __init__(self, shape, color):
        self.obj = turtle.Turtle()
        self.obj.speed(0)
        self.obj.shape(shape)
        self.obj.color(color)
        self.obj.penup()
        self.obj.goto(0,100)

    def setColor(self, color):
        self.obj.color(color)
        return

    def getPos(self):
        return self.obj.goto

    def setPos(self, x, y):
        self.obj.goto(x,y)
        return
    
    def randomPos(self):
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        self.setPos(x, y)