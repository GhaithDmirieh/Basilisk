import turtle
from turtle import RawTurtle, TurtleScreen

class Headline:
    def __init__(self, window, content, x, y):
        self.headline = RawTurtle(window)
        self.headline.speed(0)
        self.headline.shape("square")
        self.headline.color("white")
        self.headline.penup()
        self.headline.hideturtle() # Versteckter Überschrift
        self.headline.goto(0,250)
        self.headline.write("Score: 0 High Score: 0,", align= "center", font=("Courier", 18 ,"normal"))
    
    def writeHeadlineForGameOver(self):
        self.headline.clear()
        self.headline.write("Game Over", align= "center", font=("Courier", 18 ,"normal"))

    def writeNewHeadline(self, score, newScore):
        self.headline.clear()
        self.headline.write("Score:{} High Score: {}".format(score, newScore), align ="center", font=("Courier", 18 ,"normal"))
