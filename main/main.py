import turtle
import time
import random
from model.basilisk import Basilisk
from model.object import Object
from model.gamefield import Gamefield

basilisk = Basilisk("square", "red")
apple = Object("square", "white")
myGameField = Gamefield("test", "green")

def gameOver():
    for item in basilisk.body:
        if item.distance(basilisk.mouth) < 20:
            basilisk.headline.clear()
            basilisk.headline.write("Game Over", align= "center", font=("Courier", 18 ,"normal"))
            time.sleep(1)
            basilisk.mouth.goto(0,0)
            basilisk.mouth.direction = "stop"
        
            for x in basilisk.body:
                x.goto(1000, 1000)
                basilisk.body.clear()
                basilisk.score = 0
                basilisk.speed = 0.1
                basilisk.headline.clear()
                basilisk.headline.write("Score:{} High Score: {}".format(basilisk.score, basilisk.high_score), align ="center", font=("Courier", 18 ,"normal"))

