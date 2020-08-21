import time
import random
import copy
import tkinter as tk
import json
import os
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
rootWindow.title("Snake Game")
rootWindow.configure(background='green')
logo = tk.PhotoImage(file="model/resources/Logo.gif")
subWindowForGamefiled = tk.Canvas(rootWindow, width=580, height=580)
subWindowForBestList = tk.Canvas(rootWindow, width=200, height=550)
#subWindowForGamefiled.pack(side = tk.LEFT)
#subWindowForBestList.pack(side = tk.TOP)

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
headlineForGame.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())
headlineForBestList = Headline(bestListField.getRootWindow(), headlineForBestListContent, 0, 0)

tt = "Best List:\n {} --> {}\n {} --> {}\n {} --> {}\n {} --> {}\n {} --> {}".format(1, highScoreList[4], 2, highScoreList[3], 3, highScoreList[2], 4, highScoreList[1], 5, highScoreList[0])

headlineForBestList.writeNewHeadlineForBestList(tt)


def pause():
    for i in [ 5, 4, 3, 2, 1 ,0]:
        time.sleep(1)
        line = RawTurtle(myGameField.getRootWindow())
        line.speed(0)
        line.shape("square")
        line.color("white")
        line.penup()
        line.hideturtle() # Versteckter Überschrift
        line.goto(0,0)
        line.write("Waiting for %s seconds" % i , align= "center", font=("Courier", 18 ,"normal"))
        line.clear()

def getReady():
    for i in [ 5, 4, 3, 2, 1 ,0]:
        time.sleep(1)
        line = RawTurtle(myGameField.getRootWindow())
        line.speed(0)
        line.shape("square")
        line.color("white")
        line.penup()
        line.hideturtle() # Versteckter Überschrift
        line.goto(0,0)
        line.write("Get ready %s" % i , align= "center", font=("Courier", 18 ,"normal"))
        line.clear()

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


def save():
    data = {}
    data['mouth'] = {'x': basilisk.getXPos(), 'y': basilisk.getYPos()}
    data['apple'] = {'x': apple.getXPos(), 'y': apple.getYPos()}
    data['poison'] = {'x': poison.getXPos(), 'y': poison.getYPos()}
    data['body'] = basilisk.getBodyPosInListOfDic()
    data['dir'] = {'direction': basilisk.getMouthDirection()}
    data['scores'] = {'score': basilisk.getScore(), 'highScore': basilisk.getHighScore()}

    with open('lastGameData.txt', 'w') as dataFile:
        json.dump(data, dataFile)


def load(): #Diese Funktion wird nur einmal vom Hauptmenü aufgerufen. Das Button ist nur ein Test
    getReady()

    with open('lastGameData.txt') as jFile:
        data = json.load(jFile)
    
    basilisk.setMouthPos(data['mouth']['x'], data['mouth']['y'])
    poison.setPos(data['poison']['x'], data['poison']['y'])
    apple.setPos(data['apple']['x'], data['apple']['y'])
    basilisk.setMouthDirection(data['dir']['direction'])
    basilisk.setScore(data['scores']['score'])
    basilisk.setHighScore(data['scores']['highScore'])
    headlineForGame.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())

    for i in range(0, len(data['body'])):
        x = data['body'][i]['bodyBlock' + str(i)]["x"]
        y = data['body'][i]['bodyBlock' + str(i)]['y']
        basilisk.basiliskFeeded(myGameField.getRootWindow() ,gifBody)
        basilisk.setBodyBlockPos(i, x, y)
    
    os.remove("S:/git/Basilisk/lastGameData.txt")

def onePlayer():
    widget_list = all_children(rootWindow)
    for item in widget_list:
        item.pack_forget()
        
    subWindowForGamefiled.pack(side = tk.LEFT)
    subWindowForBestList.pack(side = tk.TOP)
    tk.Button(master = rootWindow, text = "Exit", command = exit , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(side = tk.RIGHT)
    tk.Button(master = rootWindow, text = "save", command = save , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(side = tk.LEFT)
    tk.Button(master = rootWindow, text = "pause", command = pause, bg='springgreen4' , activebackground = 'green', fg = 'white').pack(side = tk.RIGHT)
    tk.Button(master = rootWindow, text = "back to Menu", command = backToMenu, bg='springgreen4' , activebackground = 'green', fg = 'white').pack(side = tk.LEFT)

def LoadMenu():
    widget_list = all_children(rootWindow)
    for item in widget_list:
        item.pack_forget()
        
    subWindowForGamefiled.pack(side = tk.LEFT)
    subWindowForBestList.pack(side = tk.TOP)
    tk.Button(master = rootWindow, text = "Exit", command = exit , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(side = tk.RIGHT)
    tk.Button(master = rootWindow, text = "save", command = save , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(side = tk.LEFT)
    tk.Button(master = rootWindow, text = "pause", command = pause, bg='springgreen4' , activebackground = 'green', fg = 'white').pack(side = tk.RIGHT)
    tk.Button(master = rootWindow, text = "back to Menu", command = backToMenu, bg='springgreen4' , activebackground = 'green', fg = 'white').pack(side = tk.LEFT)
    load()

def backToMenu():
    gameOver()
    widget_list = all_children(rootWindow)
    for item in widget_list:
        item.pack_forget()
    tk.Label(rootWindow, compound = tk.CENTER,text="             Welcome to Snake Game           ",fg="white",bg= "green", font=("Helvetica", 20)).pack(side="top")
    tk.Label(rootWindow, compound = tk.CENTER,text="", image=logo,bg= "green").pack(side="top")
    tk.Button(master = rootWindow, text = "            START            ", command = onePlayer , bg='springgreen4' , activebackground = 'green', fg = 'white').pack()
    tk.Button(master = rootWindow, text = "Load last saved Game", command = LoadMenu , bg='springgreen4' , activebackground = 'green', fg = 'white').pack()
    tk.Button(master = rootWindow, text = "              EXIT             ", command = exit , bg='springgreen4' , activebackground = 'green', fg = 'white').pack()
    tk.Label(rootWindow, compound = tk.CENTER,text=" ",fg="white",bg= "green", font=("Helvetica", 30)).pack()
        
def all_children (rootWindow) :
    _list = rootWindow.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

if __name__ == "__main__":
    tk.Label(rootWindow, compound = tk.CENTER,text="             Welcome to Snake Game           ",fg="white",bg= "green", font=("Helvetica", 20)).pack(side="top")
    tk.Label(rootWindow, compound = tk.CENTER,text="", image=logo,bg= "green").pack(side="top")
    tk.Button(master = rootWindow, text = "            START            ", command = onePlayer , bg='springgreen4' , activebackground = 'green', fg = 'white').pack()
    tk.Button(master = rootWindow, text = "Load last saved Game", command = LoadMenu , bg='springgreen4' , activebackground = 'green', fg = 'white').pack()
    tk.Button(master = rootWindow, text = "              EXIT             ", command = exit , bg='springgreen4' , activebackground = 'green', fg = 'white').pack()
    tk.Label(rootWindow, compound = tk.CENTER,text=" ",fg="white",bg= "green", font=("Helvetica", 30)).pack()
    
    myGameField.gameListenToPresskey(basilisk)

    basilisk.setHighScore(highScoreList[4])
    headlineForGame.writeNewHeadline(basilisk.getScore(),highScoreList[4])

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
            basilisk.basiliskLives()

        if basilisk.basiliskEats(apple.getObj()):
            apple.randomPos() #TODO: Pos darf nicht in Snakes Körper oder Headline stehen
            poison.randomPos()
            
            
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