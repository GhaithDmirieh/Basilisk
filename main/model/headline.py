import turtle

class Headline:
    def __init__(self):
        self.headline = turtle.Turtle()
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
