import time
import random
import copy

import tkinter as tk
from turtle import RawTurtle, TurtleScreen
import tkinter.messagebox
from model.basilisk import Basilisk
from model.object import Object
from model.gamefield import Gamefield
from model.headline import Headline

highScoreList = []

try:
    f = open("highScoreList.txt", "r")
    fileContentInString = f.read()
    f.close()

    tempList =  [item for item in fileContentInString.split(',')]
    tempList.pop()

    for i in range(0, len(tempList)):
        tempList[i] = int(tempList[i])

    highScoreList = copy.deepcopy(tempList)

except:
    highScoreList = [0,0,0,0,0]

rootWindow = tk.Tk()
subWindowForGamefiled = tk.Canvas(rootWindow, width=600, height=600)
subWindowForBestList = tk.Canvas(rootWindow, width=200, height=570)
subWindowForGamefiled.pack(side = tk.LEFT)
subWindowForBestList.pack(side = tk.TOP)

headlineContent = "Score: 0 High Score: 0"
headlineForBestListContent = "Best List:"

myGameField = Gamefield(subWindowForGamefiled, "green")
bestListField = Gamefield(subWindowForBestList, "springgreen4")

gifApple = "model/resources/Apple.gif"
gifUp = "model/resources/up.gif"
gifDown = "model/resources/down.gif"
gifLeft = "model/resources/left.gif"
gifRight = "model/resources/right.gif"
gifBody = "model/resources/body.gif"
gifPoison = "model/resources/poison.gif"

imageList = [gifApple, gifUp, gifDown, gifLeft, gifRight, gifBody, gifPoison]

for image in imageList:
    myGameField.addShape(image)

basilisk = Basilisk(myGameField.getRootWindow(), gifUp)
apple = Object(myGameField.getRootWindow(), gifApple)
poison = Object(myGameField.getRootWindow(), gifPoison)

poison.setPos(0, -100)

headlineForGame = Headline(myGameField.getRootWindow(), headlineContent, 0, 250)
headlineForBestList = Headline(bestListField.getRootWindow(), headlineForBestListContent, 0, 0)

tt = "Best List:\n {} --> {}\n {} --> {}\n {} --> {}\n {} --> {}\n {} --> {}".format(1, highScoreList[4], 2, highScoreList[3], 3, highScoreList[2], 4, highScoreList[1], 5, highScoreList[0])

headlineForBestList.writeNewHeadlineForBestList(tt)

def gameOver():
    headlineForGame.writeHeadlineForGameOver()
    time.sleep(1)
    basilisk.basiliskGoHome()
    basilisk.basiliskDeleteBody()
    basilisk.setScore(0)
    basilisk.setSpeed(0.1)
    headlineForGame.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())
    saveHighScoreInFile()

def saveHighScoreInFile():
        if basilisk.getHighScore() in highScoreList:
            return
        else: # Erweitere die Liste mit einem Element dann sortiere sie und lösche das Element mit dem niedrigsten Wert
            highScoreList.append(basilisk.getHighScore())
            sorted(highScoreList)
            if len(highScoreList) == 6:
                del(highScoreList[0])
                temp = "Best List:\n {} --> {}\n {} --> {}\n {} --> {}\n {} --> {}\n {} --> {}".format(1, highScoreList[4], 2, highScoreList[3], 3, highScoreList[2], 4, highScoreList[1], 5, highScoreList[0])
                headlineForBestList.writeNewHeadlineForBestList(temp)
                fileR = open("highScoreList.txt", "w")
                for y in highScoreList:
                    fileR.write("{},".format(str(y)))
                fileR.close()

def exit():
    rootWindow.destroy() #TODO: go to startmenü statt spiel verlassen

if __name__ == "__main__":

    tk.Button(master = rootWindow, text = "Exit", command = exit , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(side = tk.RIGHT)

    myGameField.gameListenToPresskey(basilisk)

    while True:
        myGameField.gamefieldUpdate()

        if basilisk.basiliskEats(poison.getObj()):
            basilisk.basiliskPoisoned()
            poison.randomPos()
            basilisk.setSpeed(basilisk.getSpeed() + 0.001)
            basilisk.setScore(basilisk.getScore() - 10)
            headlineForGame.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())
            

        if basilisk.basiliskIsDead():
            gameOver()
        if basilisk.basiliskEats(apple.getObj()):
            apple.randomPos() #TODO: Pos darf nicht in Snakes Körper oder Headline stehen
            
            basilisk.basiliskFeeded(myGameField.getRootWindow() ,gifBody)
            basilisk.setSpeed(basilisk.getSpeed() - 0.001)
            basilisk.setScore(basilisk.getScore() + 10)
            headlineForGame.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())

            if basilisk.getScore() > basilisk.getHighScore():
                basilisk.setHighScore(basilisk.getScore())
                headlineForGame.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())
                
        basilisk.bodyFollowMouth()
        basilisk.move()
        time.sleep(basilisk.getSpeed())

    myGameField.gamefieldMainloop()