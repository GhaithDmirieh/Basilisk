import turtle
import time
from turtle import RawTurtle, TurtleScreen

class Basilisk:

    def __init__(self, window, shape):
        self.speed = 0.1
        self.score = 0
        self.high_score = 0

        self.mouth = RawTurtle(window)
        self.mouth.speed(0)
        self.mouth.shape(shape)
        self.mouth.home() #Home ist clearer than goto(0,0)
        self.mouth.direction = "stop"
        self.mouth.penup()

        self.body = []

    def getSpeed(self):
        return self.speed
    
    def getScore(self):
        return self.score
    
    def getHighScore(self):
        return self.high_score
    
    def setSpeed(self, speed):
        self.speed = speed
    
    def setScore(self, score):
        self.score = score
    
    def setHighScore(self, highScore):
        self.high_score = highScore


    def moveUpwards(self):
        if self.mouth.direction != "down":
            self.mouth.direction = "up"

    def moveDownwards(self):
        if self.mouth.direction != "up":
            self.mouth.direction = "down"

    def moveLeftwards(self):
        if self.mouth.direction != "right":
            self.mouth.direction = "left"

    def moveRightwards(self):
        if self.mouth.direction != "left":
            self.mouth.direction = "right"
    
    def move(self):
        if self.mouth.direction == "up":
            self.mouth.sety(self.mouth.ycor() + 20)
            
        if self.mouth.direction == "down":
            self.mouth.sety(self.mouth.ycor() - 20)
        
        if self.mouth.direction == "left":
            self.mouth.setx(self.mouth.xcor() - 20)
        
        if self.mouth.direction == "right":
            self.mouth.setx(self.mouth.xcor() + 20)
    
    def bodyFollowMouth(self):
        for index in range(len(self.body)-1 , 0, -1):
            self.body[index].goto(self.body[index-1].xcor(), self.body[index-1].ycor())
        if len(self.body) > 0:
            self.body[0].goto(self.mouth.xcor(),self.mouth.ycor())

    def basiliskFeeded(self, window, shape):
        oneBodyBlock = RawTurtle(window)
        oneBodyBlock.speed(0)
        oneBodyBlock.shape(self.mouth.shape())
        oneBodyBlock.color(oneBodyBlockColor)
        oneBodyBlock.penup()
        self.body.append(oneBodyBlock)
    
    def basiliskIsDead(self):
        basiliskPushTheWall = self.mouth.xcor() > 290 or self.mouth.xcor() < -290 or self.mouth.ycor() > 290 or self.mouth.ycor() < -290
        
        if basiliskPushTheWall:
            return True
        
        for item in self.body:
            basiliskEatsHerself = item.distance(self.mouth) < 20
            if basiliskEatsHerself:
                return True
    
    def basiliskEats(self, obj):
        return self.mouth.distance(obj) < 20

    def basiliskGoHome(self):
        self.mouth.home()
        self.mouth.direction = "stop"
    
    def basiliskDeleteBody(self):
        for item in self.body:
            item.goto(1000, 1000) # Gibt es keine bessere Weise !
        self.body.clear()

