import turtle
import random
from turtle import RawTurtle, TurtleScreen

class Object:
    def __init__(self, window, shape):
        self.obj = RawTurtle(window)
        self.obj.speed(0)
        self.obj.shape(shape)
        self.obj.penup()
        self.obj.goto(0,100)

    def getObj(self):
        return self.obj

    def setPos(self, x, y):
        self.obj.goto(x,y)
        self.obj.sety(self.obj.ycor()-(self.obj.ycor()%20))
        self.obj.setx(self.obj.xcor()-(self.obj.xcor()%20))
        return
    
    def randomPos(self): #Pos darf nicht in Snakes Körper oder Headline stehen
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        self.setPos(x, y)