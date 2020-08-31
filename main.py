import time
import random
import copy
import tkinter as tk
import json
import os
from turtle import RawTurtle, TurtleScreen
from model.basilisk import Basilisk
from model.object import Object
from model.gamefield import Gamefield
from model.headline import Headline
from tkinter import messagebox
from winsound import PlaySound, SND_FILENAME

highScoreList = []

# lade HighScores und stelle sie in der Liste bereit.
try:
    f = open("highScoreList.txt", "r")
    fileContentInString = f.read()
    f.close()

    tempList =  [item for item in fileContentInString.split(',')]
    tempList.pop()

    for tempItem in range(0, len(tempList)):
        tempList[tempItem] = int(tempList[tempItem])

    highScoreList = copy.deepcopy(tempList)

except:
    highScoreList = [0,0,0,0,0]

rootWindow = tk.Tk()
rootWindow.resizable(0,0)
rootWindow.title("Basilisk Game")
rootWindow.configure(background='green')

logo = tk.PhotoImage(file="model/resources/Logo.gif")

subWindowForGamefiled = tk.Canvas(rootWindow, width=580, height=580)
subWindowForBestList = tk.Canvas(rootWindow, width=200, height=450)

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
gifBody2 = "model/resources/body2.gif"
gifPoison = "model/resources/poison.gif"

imageList = [gifApple, gifUp, gifDown, gifLeft, gifRight, gifBody, gifBody2, gifPoison]

# fügt alle GIFs in einer liste ein und fügt sie als Shapes dem GameField hinzu.
for image in imageList:
    myGameField.addShape(image)

basilisk2 = Basilisk(myGameField.getRootWindow(), gifUp)
basilisk2.setMouthPos(100, 0)


basilisk = Basilisk(myGameField.getRootWindow(), gifUp)
apple = Object(myGameField.getRootWindow(), gifApple)
poison = Object(myGameField.getRootWindow(), gifPoison)

poison.setPos(0, -100)

# headlineForGame ist ein Label in dem Score und HighScore erscheinen sollen.
headlineForGame = Headline(myGameField.getRootWindow(), headlineContent, 0, 250)
headlineForGame.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())
headlineForBestList = Headline(bestListField.getRootWindow(), headlineForBestListContent, 0, 0)

tt = "Best List:\n {} --> {}\n {} --> {}\n {} --> {}\n {} --> {}\n {} --> {}".format(1, highScoreList[4], 2, highScoreList[3], 3, highScoreList[2], 4, highScoreList[1], 5, highScoreList[0])
headlineForBestList.writeNewHeadlineForBestList(tt)

# 5 Sekunden Pause Funktion.
def pause():
    for i in [ 5, 4, 3, 2, 1 ,0]:
        time.sleep(1)
        line = RawTurtle(myGameField.getRootWindow())
        line.speed(0)
        line.shape("square")
        line.color("white")
        line.penup()
        line.hideturtle() # Versteckte Überschrift
        line.goto(0,0)
        line.write("Waiting for %s seconds" % i , align= "center", font=("Courier", 18 ,"normal"))
        line.clear()

# nach dem Laden der letzten gespeicherten Sitzung kommt getReady Pause von 5 Sekunden.
def getReady():
    for i in [ 5, 4, 3, 2, 1 ,0]:
        time.sleep(1)
        line = RawTurtle(myGameField.getRootWindow())
        line.speed(0)
        line.shape("square")
        line.color("white")
        line.penup()
        line.hideturtle() # Versteckte Überschrift
        line.goto(0,0)
        line.write("Get ready %s" % i , align= "center", font=("Courier", 18 ,"normal"))
        line.clear()

# Die Funktion kümmert sich nur um das, was nach dem Beenden geschieht (Alles wieder auf den originalen Stand stellen).
def gameOver():
    for itemOfHighScoreList in highScoreList:
        if basilisk.getScore() > itemOfHighScoreList and basilisk.getScore() < basilisk.getHighScore():
            basilisk.setTempScore(basilisk.getScore())

    headlineForGame.writeHeadlineForGameOver()
    play()
    time.sleep(1)
    basilisk.basiliskGoHome()
    basilisk.basiliskDeleteBody()
    basilisk.setScore(0)
    basilisk.setSpeed(0.1)
    headlineForGame.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())
    saveHighScoreInFile()
    apple.setPos(0,100)
    poison.setPos(0,-100)

# Gameover für die erste Schlange im zwei Spieler Modus.
def gameOverForFirstBasiliskInTwoPlayerMode():
    basilisk.basiliskDeleteBody()
    basilisk.basiliskGoHome()
    basilisk.setSpeed(0.1)
    
# Gameover für die zweite Schlange im zwei Spieler Modus.
def gameOverForSecondBasiliskInTowPlayerMode():
    basilisk2.basiliskDeleteBody()
    basilisk2.basiliskGoHome()
    basilisk2.setSpeed(0.1)

# Speichere die Liste von highscore in text file.
def saveHighScoreInFile():
        if basilisk.getTempScore() > 1 and basilisk.getTempScore() not in highScoreList:
            highScoreList.append(basilisk.getTempScore())
            highScoreList [:] = sorted(highScoreList)
            basilisk.setTempScore(1)
            if len(highScoreList) == 6:
                del(highScoreList[0])
                temp0 = "Best List:\n {} --> {}\n {} --> {}\n {} --> {}\n {} --> {}\n {} --> {}".format(1, highScoreList[4], 2, highScoreList[3], 3, highScoreList[2], 4, highScoreList[1], 5, highScoreList[0])
                headlineForBestList.writeNewHeadlineForBestList(temp0)
                
                file0 = open("highScoreList.txt", "w")
                for number in highScoreList:
                    file0.write("{},".format(str(number)))
                file0.close()
        
        if basilisk.getHighScore() in highScoreList:
            return
        
        else : # Erweitere die Liste mit einem Element dann sortiere sie und lösche das Element mit dem niedrigsten Wert.
            highScoreList.append(basilisk.getHighScore())
            highScoreList [:] = sorted(highScoreList)
            if len(highScoreList) == 6:
                del(highScoreList[0])
                temp = "Best List:\n {} --> {}\n {} --> {}\n {} --> {}\n {} --> {}\n {} --> {}".format(1, highScoreList[4], 2, highScoreList[3], 3, highScoreList[2], 4, highScoreList[1], 5, highScoreList[0])
                headlineForBestList.writeNewHeadlineForBestList(temp)
                fileR = open("highScoreList.txt", "w")
                for y in highScoreList:
                    fileR.write("{},".format(str(y)))
                fileR.close()

def exit():
    rootWindow.destroy()

# save Funktion Speichert die eigenschaften der Sitzung (Schlange und Obst und Gift Position, Schlange länge, Score und die Geschwindigkeit).
def save():
    data = {}
    data['mouth'] = {'x': basilisk.getXPos(), 'y': basilisk.getYPos()}
    data['apple'] = {'x': apple.getXPos(), 'y': apple.getYPos()}
    data['poison'] = {'x': poison.getXPos(), 'y': poison.getYPos()}
    data['dir'] = {'direction': basilisk.getMouthDirection()}
    data['scores'] = {'score': basilisk.getScore(), 'highScore': basilisk.getHighScore()}
    data['speed'] = {'Speed': basilisk.getSpeed()}
    if basilisk.getBodyLen() > 0:
        data['body'] = basilisk.getBodyPosInListOfDic()

    with open('lastGameData.txt', 'w') as dataFile:
        json.dump(data, dataFile)


# Lade die Daten der letzten Sitzung für die Schlange und lösche danach diese Daten. Dann starte das Spiel in 1 Spieler Modus.
def load():

    data = {}
    try:
        with open('lastGameData.txt') as jFile:
            dataFromJson = json.load(jFile)
            data = dataFromJson
            
    except:
        messagebox.showinfo("Error", "There is no saved game")
        startForOnePlayer()
        return
    
    getReady()

    basilisk.setMouthPos(data['mouth']['x'], data['mouth']['y'])
    poison.setPos(data['poison']['x'], data['poison']['y'])
    apple.setPos(data['apple']['x'], data['apple']['y'])
    basilisk.setMouthDirection(data['dir']['direction'])
    basilisk.setScore(data['scores']['score'])
    basilisk.setHighScore(data['scores']['highScore'])
    basilisk.setSpeed(data['speed']['Speed'])
    headlineForGame.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())

    if 'body' in data:
        for i in range(0, len(data['body'])):
            x = data['body'][i]['bodyBlock' + str(i)]["x"]
            y = data['body'][i]['bodyBlock' + str(i)]['y']
            basilisk.basiliskFeeded(myGameField.getRootWindow() ,gifBody)
            basilisk.setBodyBlockPos(i, x, y)

    os.remove("S:/git/Basilisk/lastGameData.txt")

    while True:
        try:
            myGameField.gamefieldUpdate()
            onePlayer()
        except:
            return

# In der loadLastGame Funktion werden alle widgets des RootWindow gelöscht, das subWindowForGamefiled mit den Buttons angezeigt und der Funktion load() aufgerufen.
def loadLastGame():
    widget_list = all_children(rootWindow)
    for item in widget_list:
        item.pack_forget()

    subWindowForGamefiled.pack(side = tk.LEFT)
    basilisk2.setMouthPos(1000,1000)
    basilisk2.hideMouth()
    subWindowForBestList.pack(side = tk.TOP)
    tk.Button(master = rootWindow, text = "Pause", command = pause, bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    tk.Button(master = rootWindow, text = "Save", command = save , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    tk.Button(master = rootWindow, text = "Back to Menu", command = backToMenu, bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    tk.Button(master = rootWindow, text = "Exit", command = exit , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    load()

# In der backToMenu Funktion werden alle widgets des RootWindow gelöscht und das Hauptmenü mit den Buttons angezeigt.
def backToMenu():
    gameOver()
    widget_list = all_children(rootWindow)
    for item in widget_list:
        item.pack_forget()
    tk.Label(rootWindow, compound = tk.CENTER,text="             Welcome to Basilisk Game           \nHigh Score: {}".format(highScoreList[4]),fg="white",bg= "green", font=("Helvetica", 20)).pack(side="top")
    tk.Label(rootWindow, compound = tk.CENTER,text="", image=logo,bg= "green").pack(side="top")
    tk.Button(master = rootWindow, text = "One Player Mode", command = startForOnePlayer , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    tk.Button(master = rootWindow, text = "Two Player Mode", command = startForTwoPlayer , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)    
    tk.Button(master = rootWindow, text = "Load last Game", command = loadLastGame , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    tk.Button(master = rootWindow, text = "Exit", command = exit , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)

# Gib eine Liste von allen widgets zurück.
def all_children (rootWindow) :
    _list = rootWindow.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

# Game over Musik
def play():
    return PlaySound("model/resources/gameover.wav", SND_FILENAME)

# Bereite alle widgets vor und starte das Spiel für 1 Spieler.
def startForOnePlayer():
    widget_list = all_children(rootWindow)
    for item in widget_list:
        item.pack_forget()
        
    subWindowForGamefiled.pack(side = tk.LEFT)
    basilisk2.setMouthPos(1000,1000)
    basilisk2.hideMouth()
    subWindowForBestList.pack(side = tk.TOP)
    tk.Button(master = rootWindow, text = "Pause", command = pause, bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    tk.Button(master = rootWindow, text = "Save", command = save , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    tk.Button(master = rootWindow, text = "Back to Menu", command = backToMenu, bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    tk.Button(master = rootWindow, text = "Exit", command = exit , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    
    while True:
        try:
            myGameField.gamefieldUpdate()
            onePlayer()
        except:
            return

# Bereite alle widgets vor und starte das Spiel für 2 Spieler.
def startForTwoPlayer():

    widget_list = all_children(rootWindow)
    for item in widget_list:
        item.pack_forget()

    headlineForGame.clearHideline()

    basilisk2.showMouth()
    subWindowForGamefiled.pack(side = tk.TOP)
    tk.Button(master = rootWindow, text = "           Exit          ", command = exit , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(side = tk.BOTTOM , fill=tk.BOTH) 
    tk.Button(master = rootWindow, text = "Pause", command = pause, bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    poison.setPos(1000,1000)
    poison.hideObj()

    apple.randomPos()
    basilisk.setMouthPos(-60,0)
    basilisk2.setMouthPos(60,0)

    while True:
        try:
            myGameField.gamefieldUpdate()
            twoPlayer()
        except:
            return

# Prüfe ob die erste Schlange die Zweite beißt.
def basilisk1EatsBasilisk2():
    for oneBlock in basilisk2.getBodyList():
        dead = oneBlock.distance(basilisk.getMouth()) < 20
        if dead:
            return True

# Prüfe ob die zweite Schlange die Erste beißt.
def basilisk2EatsBasilisk1():
    for oneBlock in basilisk.getBodyList():
        dead = oneBlock.distance(basilisk2.getMouth()) < 20
        if dead:
            return True

# Prüfe ob im Zweispielermodus die zufällige Position des Apfels im Körper einer Schlage erscheint, falls ja, weise ihr eine neue zufällige Position zu.
def checkIfAppleInBasiliskForTowPlayer():
    for oneBlock in basilisk2.getBodyList():
        isIn = oneBlock.distance(apple.getObj()) < 20
        if isIn:
            return True

    for oneBlock in basilisk.getBodyList():
        isIn = oneBlock.distance(apple.getObj()) < 20
        if isIn:
            return True

# Prüfe ob im Einspielermodus die zufällige Position des Apfels im Körper einer Schlage erscheint, falls ja, weise ihr eine neue zufällige Position zu.
def checkIfAppleInBasiliskForOnePlayer():
    for oneBlock in basilisk.getBodyList():
        isIn = oneBlock.distance(apple.getObj()) < 20 or oneBlock.distance(poison.getObj()) < 20
        if isIn:
            return True
# Eigenschaften des Ein-Spieler-Modus.
def onePlayer():
    if basilisk.basiliskEats(poison.getObj()):
        basilisk.basiliskPoisoned()
        poison.randomPos()
        apple.randomPos()

        if checkIfAppleInBasiliskForOnePlayer():
            poison.randomPos()
            apple.randomPos()

        basilisk.setSpeed(basilisk.getSpeed() + 0.001)
        basilisk.setScore(basilisk.getScore() - 10)
        headlineForGame.writeNewHeadline(basilisk.getScore(), basilisk.getHighScore())
        
    basilisk.basiliskPushTheWall()
    
    if basilisk.basiliskIsDead():
        gameOver()
        basilisk.basiliskLives()

    if basilisk.basiliskEats(apple.getObj()):
        apple.randomPos()
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
    
# Eigenschaften des Zwei-Spieler-Modus.
def twoPlayer():
    basilisk.basiliskPushTheWall()
    basilisk2.basiliskPushTheWall()


    
    if basilisk.basiliskIsDead() or basilisk1EatsBasilisk2():
        gameOverForFirstBasiliskInTwoPlayerMode()
        basilisk.basiliskLives()

    if basilisk2.basiliskIsDead() or basilisk2EatsBasilisk1():
        gameOverForSecondBasiliskInTowPlayerMode()
        basilisk2.basiliskLives()
    
    if basilisk.getMouth().distance(basilisk2.getMouth()) < 15 or basilisk2.getMouth().distance(basilisk.getMouth()) < 15:
        gameOverForFirstBasiliskInTwoPlayerMode()
        gameOverForSecondBasiliskInTowPlayerMode()
        
        basilisk.basiliskLives()
        basilisk.setMouthPos(-60,0)

        basilisk2.basiliskLives()
        basilisk2.setMouthPos(60,0)


    if basilisk.basiliskEats(apple.getObj()):
        apple.randomPos()
        
        if checkIfAppleInBasiliskForTowPlayer():
            apple.randomPos()
        
        for oneBlock in basilisk.getBodyList():
            if apple.getObj().distance(oneBlock) < 20 :
                apple.randomPos()
                
        basilisk.basiliskFeeded(myGameField.getRootWindow() ,gifBody)
        

    if basilisk2.basiliskEats(apple.getObj()):
        apple.randomPos() 
        
        for oneBlock in basilisk2.getBodyList():
            if apple.getObj().distance(oneBlock) < 20 :
                apple.randomPos()
                
        basilisk2.basiliskFeeded(myGameField.getRootWindow() ,gifBody2)
        
    basilisk.bodyFollowMouth()
    basilisk.move()
    basilisk2.bodyFollowMouth()
    basilisk2.move()
    time.sleep(0.1)

if __name__ == "__main__":
    #
    tk.Label(rootWindow, compound = tk.CENTER,text="             Welcome to Basilisk Game           \nHigh Score: {}".format(highScoreList[4]),fg="white",bg= "green", font=("Helvetica", 20)).pack(side="top")
    tk.Label(rootWindow, compound = tk.CENTER,text="", image=logo,bg= "green").pack(side="top")
    tk.Button(master = rootWindow, text = "One Player Mode", command = startForOnePlayer , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    tk.Button(master = rootWindow, text = "Two Player Mode", command = startForTwoPlayer , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    tk.Button(master = rootWindow, text = "Load last Game", command = loadLastGame , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
    tk.Button(master = rootWindow, text = "Exit", command = exit , bg='springgreen4' , activebackground = 'green', fg = 'white').pack(fill=tk.BOTH)
   
    myGameField.gameListenToPresskey(basilisk)

    # Die zweite Schlange im Einspielermodus nicht aktivieren.
    if basilisk2.isVisible():
        myGameField.gameListenToPresskeyForTowPlayer(basilisk2)

    basilisk.setHighScore(highScoreList[4])
    headlineForGame.writeNewHeadline(basilisk.getScore(),highScoreList[4])

    myGameField.gamefieldMainloop()
