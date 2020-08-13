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

    def getObj(self):
        return self.obj

    def setColor(self, color):
        self.obj.color(color)
        return

    def setPos(self, x, y):
        self.obj.goto(x,y)
        return
    
    def randomPos(self): #Pos darf nicht in Snakes Körper oder Headline stehen
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        self.setPos(x, y)