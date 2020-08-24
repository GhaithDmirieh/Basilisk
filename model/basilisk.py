import turtle
import time
from turtle import RawTurtle, TurtleScreen

class Basilisk:

    def __init__(self, window, shape):
        self.speed = 0.1
        self.score = 0
        self.highScore = 0
        
        self.mouth = RawTurtle(window)
        self.mouth.speed(0)
        self.mouth.shape(shape)
        self.mouth.home() # Home ist clearer than goto(0,0)
        self.mouth.direction = "stop"
        self.mouth.penup()
        
        self.deadFromPoison = False

        self.body = []

    def getBodyLen(self):
        return len(self.body)

    def getYPos(self):
        return self.mouth.ycor()
        
    def getXPos(self):
        return self.mouth.xcor()

    def setMouthPos(self, x, y):
        self.mouth.goto(x,y)

    def getSpeed(self):
        return self.speed
    
    def getScore(self):
        return self.score
    
    def getHighScore(self):
        return self.highScore
    
    def setSpeed(self, speed):
        self.speed = speed
    
    def setScore(self, score):
        self.score = score
    
    def setHighScore(self, highScore):
        self.highScore = highScore

    def getMouthDirection(self):
        return self.mouth.direction

    def setMouthDirection(self, mouthDirection):
        if mouthDirection == "left":
            self.moveLeftwards()
        elif mouthDirection == "right":
            self.moveRightwards()
        elif mouthDirection == "up":
            self.moveUpwards()
        else:
            self.moveDownwards()

    def moveUpwards(self):
        gifUp = "model/resources/up.gif"
        if self.mouth.direction != "down":
            self.mouth.direction = "up"
            self.mouth.shape(gifUp)

    def moveDownwards(self):
        gifDown = "model/resources/down.gif"
        if self.mouth.direction != "up":
            self.mouth.direction = "down"
            self.mouth.shape(gifDown)

    def moveLeftwards(self):
        gifLeft = "model/resources/left.gif"
        if self.mouth.direction != "right":
            self.mouth.direction = "left"
            self.mouth.shape(gifLeft)

    def moveRightwards(self):
        gifRight = "model/resources/right.gif"
        if self.mouth.direction != "left":
            self.mouth.direction = "right"
            self.mouth.shape(gifRight)
    
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
        oneBodyBlock.shape(shape)
        oneBodyBlock.penup()
        self.body.append(oneBodyBlock)
    
    def getBodyPosInListOfDic(self):
        if len(self.body) > 0:
            allBlockskPos = []
            for i in range(0, len(self.body)):
                x = self.body[i].xcor()
                y = self.body[i].ycor()
                allBlockskPos.append({"bodyBlock" + str(i) : {'x': x, 'y': y}})

            return allBlockskPos

    def setBodyBlockPos(self, i, x, y):
        self.body[i].goto(x,y)

    #Wird noch verbessert
    def basiliskPoisoned(self):
        if len(self.body) > 0:
            self.body[-1].goto(1000,1000)
            self.body.pop()
            return
        else:
            self.deadFromPoison = True
    
    def basiliskLives(self):
        self.deadFromPoison = False

    def basiliskPushTheWall(self):
        if self.mouth.xcor() > 290:
            self.mouth.setx (self.mouth.xcor() -580)
        elif self.mouth.xcor() < -290:
            self.mouth.setx (self.mouth.xcor() +580)
        elif self.mouth.ycor() > 290:
            self.mouth.sety (self.mouth.ycor() -580)
        elif self.mouth.ycor() < -290:
            self.mouth.sety (self.mouth.ycor() +580)
            
    def basiliskIsDead(self):
        #basiliskPushTheWall = self.mouth.xcor() > 290 or self.mouth.xcor() < -290 or self.mouth.ycor() > 290 or self.mouth.ycor() < -290
        
        #if basiliskPushTheWall or
        if self.deadFromPoison:
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

