import turtle
import time

class Basilisk:
    
    def __init__(self, shape, mouthColor):
        self.speed = 0.1
        self.score = 0
        self.high_score = 0

        self.mouth = turtle.Turtle()
        self.mouth.speed(0)
        self.mouth.shape(shape)
        self.mouth.color(mouthColor)
        self.mouth.goto(0,0) # Anfangsposition
        self.mouth.direction = "stop"
        self.mouth.penup()

        self.body = []

        self.headline = turtle.Turtle()
        self.headline.speed(0)
        self.headline.shape("square")
        self.headline.color("white")
        self.headline.penup()
        self.headline.hideturtle() # Versteckter Überschrift
        self.headline.goto(0,250)
        self.headline.write("Score: 0 High Score: 0,", align= "center", font=("Courier", 18 ,"normal"))

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
    
    def bodyfollowMouth(self):
        for index in range(len(self.body)-1 , 0, -1):
            self.body[index].goto(self.body[index-1].xcor(), self.body[index-1].ycor())
        if len(self.body) > 0:
            self.body[0].goto(self.mouth.xcor(),self.mouth.ycor())

    def basiliskFeeded(self, oneBodyBlockColor):
        oneBodyBlock = turtle.Turtle()
        oneBodyBlock.speed(0)
        oneBodyBlock.shape(self.mouth.shape())
        oneBodyBlock.color(oneBodyBlockColor)
        oneBodyBlock.penup()
        self.body.append(oneBodyBlock)

