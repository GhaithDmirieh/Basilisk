import time
import random

import tkinter as tk
from turtle import RawTurtle, TurtleScreen
import tkinter.messagebox


from model.basilisk import Basilisk
from model.object import Object
from model.gamefield import Gamefield
from model.headline import Headline

highScoreList = [0,0,0,0,0]

#try:
#    f = open("text.txt", "r")
#    fileContentInString = f.read()
#    tempList =  [item for item in fileContentInString.split(',')]
#    tempList.pop()
#
#    for i in range(0, len(tempList) -1):
#        tempList[i] = tempList[i].strip(',')
#        int(tempList[i])
#        highScoreList[i] = tempList[i]
#    f.close()
#except:
#    highScoreList = [0,0,0,0,0] # temp

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

imageList = [gifApple, gifUp, gifDown, gifLeft, gifRight, gifBody]

for image in imageList:
    myGameField.addShape(image)

basilisk = Basilisk(myGameField.getRootWindow(), gifUp)
apple = Object(myGameField.getRootWindow(), gifApple)

headlineForGame = Headline(myGameField.getRootWindow(), headlineContent, 0, 250)
headlineForBestList = Headline(bestListField.getRootWindow(), headlineForBestListContent, 0, 0)

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
                fileR = open("text.txt", "w")
                for y in highScoreList:
                    fileR.write("{},".format(str(y)))
                fileR.close()

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
                headlineForGame.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())
                
        basilisk.bodyFollowMouth()
        basilisk.move()
        time.sleep(basilisk.getSpeed())

    myGameField.gamefieldMainloop()