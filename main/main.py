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

if __name__ == "__main__":

    myGameField.gameListenToPresskey(basilisk)

    while True:
        myGameField.gamefieldUpdate()
        
        if basilisk.basiliskIsDead():
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
