import time
import random

import tkinter as tk
from turtle import RawTurtle, TurtleScreen
import tkinter.messagebox


from model.basilisk import Basilisk
from model.object import Object
from model.gamefield import Gamefield
from model.headline import Headline

basilisk = Basilisk("square", "red")
apple = Object("square", "white")
myGameField = Gamefield("test", "green")
myHeadline = Headline()

gifApple = "model/resources/Apple.gif"
gifUp = "model/resources/up.gif"
gifDown = "model/resources/down.gif"
gifLeft = "model/resources/left.gif"
gifRight = "model/resources/right.gif"
gifBody = "model/resources/body.gif"

imageList = [gifApple, gifUp, gifDown, gifLeft, gifRight, gifBody]

for image in imageList:
    myGameField.addShape(image)

basilisk = Basilisk(myGameField.getRootWindow(), gifUp)
apple = Object(myGameField.getRootWindow(), gifApple)

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
            
            
            basilisk.basiliskFeeded(myGameField.getRootWindow() ,gifBody)
            basilisk.setSpeed(basilisk.getSpeed() - 0.001)
            basilisk.setScore(basilisk.getScore() + 10)

            if basilisk.getScore() > basilisk.getHighScore():
                basilisk.setHighScore(basilisk.getScore())
                myHeadline.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())

        basilisk.bodyFollowMouth()
        basilisk.move()

        time.sleep(basilisk.getSpeed())
    myGameField.gamefieldMainloop()