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
        self.headline.goto(x, y)
        self.headline.write(content, align= "center", font=("Courier", 18 ,"normal"))
    
    def writeHeadlineForGameOver(self):
        self.headline.clear()
        self.headline.write("Game Over", align= "center", font=("Courier", 18 ,"normal"))

    def writeNewHeadline(self, score, newScore):
        self.headline.clear()
        self.headline.write("Score:{} High Score: {}".format(score, newScore), align ="center", font=("Courier", 18 ,"normal"))
    
    def writeNewHeadlineForBestList(self, content):
        self.headline.clear()
        self.headline.write(content , align ="center", font=("Courier", 18 ,"normal"))
#"besten Liste\n{}".format(number)