import turtle
from turtle import RawTurtle, TurtleScreen

class Headline:
    """Die Klasse beschreibt das Aussehen einer Headline zum Anzeigen des Scores, HighScores, und der HighScoreListe."""
    def __init__(self, window, content, x, y):
        self.headline = RawTurtle(window)
        self.headline.speed(0)
        self.headline.shape("square")
        self.headline.color("white")
        self.headline.penup()
        self.headline.hideturtle()
        self.headline.goto(x, y)
        self.headline.write(content, align= "center", font=("Courier", 18 ,"normal"))
    
    def setPos(self, x, y):
        self.headline.goto(x,y)

    def writeHeadlineForGameOver(self):
        self.headline.clear()
        self.headline.write("Game Over", align= "center", font=("Courier", 18 ,"normal"))

    def writeNewHeadline(self, score, newScore):
        self.headline.clear()
        self.headline.write("Score:{} High Score: {}".format(score, newScore), align ="center", font=("Courier", 18 ,"normal"))
    
    def clearHideline(self):
        self.headline.clear()

    def writeNewHeadlineForBestList(self, content):
        self.headline.clear()
        self.headline.write(content , align ="center", font=("Courier", 18 ,"normal"))
