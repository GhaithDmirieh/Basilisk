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

#TODO: Es darf nicht auf class-Attribute hier  zugegriffen werden

def gameOver():
    myHeadline.writeHeadlineForGameOver()
    time.sleep(1)
    basilisk.basiliskGoHome()
    basilisk.basiliskDeleteBody()
    basilisk.setScore(0)
    basilisk.setSpeed(0.1)
    myHeadline.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())

if __name__ == "__main__":

    myGameField.gameListenToPresskey(basilisk)

    while True:
        myGameField.gamefieldUpdate()

        if basilisk.basiliskIsDead():
            gameOver()
        if basilisk.basiliskEats(apple.getObj()):
            apple.randomPos() #TODO: Pos darf nicht in Snakes Körper oder Headline stehen
            basilisk.basiliskFeeded("black")
            basilisk.setSpeed(basilisk.getSpeed() - 0.001)
            basilisk.setScore(basilisk.getScore() + 10)

            if basilisk.getScore() > basilisk.getHighScore():
                basilisk.setHighScore(basilisk.getScore())
                myHeadline.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())

        basilisk.bodyFollowMouth()
        basilisk.move()

        time.sleep(basilisk.getSpeed())
    myGameField.rootWindow.mainloop()
