import turtle
import time
import random
from model.basilisk import Basilisk
from model.object import Object
from model.gamefield import Gamefield
from model.headline import Headline

basilisk = Basilisk("square", "red")
apple = Object("square", "white")
myGameField = Gamefield("test", "green")
myHeadline = Headline()

def gameOver():
    for item in basilisk.body:
        if item.distance(basilisk.mouth) < 20:
            myHeadline.writeHeadlineForGameOver()
            time.sleep(1)
            basilisk.mouth.home()
            basilisk.mouth.direction = "stop"
        
            for x in basilisk.body:
                x.goto(1000, 1000)
                basilisk.body.clear()
                basilisk.score = 0
                basilisk.speed = 0.1
                myHeadline.writeNewHeadline(basilisk.score, basilisk.high_score)

if __name__ == "__main__":

    myGameField.gameListenToPresskey(basilisk)

    while True:
        myGameField.rootWindow.update()
        endGame = basilisk.mouth.xcor() > 290 or basilisk.mouth.xcor() < -290 or basilisk.mouth.ycor() > 290 or basilisk.mouth.ycor() < -290
        if endGame:
            myHeadline.writeHeadlineForGameOver()
            time.sleep(1)
            basilisk.mouth.home()
            basilisk.mouth.direction = "stop"
        
            for item in basilisk.body:
                item.goto(1000, 1000)
            basilisk.body.clear()

            basilisk.score = 0
            basilisk.speed = 0.1
            myHeadline.writeNewHeadline(basilisk.score, basilisk.high_score)

        if basilisk.mouth.distance(apple.obj) < 20:
            apple.randomPos() #TODO: Pos darf nicht in Snakes Körper oder Headline stehen

            basilisk.basiliskFeeded("black")

            basilisk.speed -= 0.001
            basilisk.score += 10

            if basilisk.score > basilisk.high_score:
                basilisk.high_score = basilisk.score
                myHeadline.writeNewHeadline(basilisk.score, basilisk.high_score)

        basilisk.bodyfollowMouth()
        basilisk.move()
        gameOver()

        time.sleep(basilisk.speed)
    myGameField.rootWindow.mainloop()
