import turtle
from turtle import RawTurtle, TurtleScreen

class Gamefield:
    def __init__(self, tkFrame, backgroundColor):
        self.rootWindow = TurtleScreen(tkFrame)
        self.rootWindow.bgcolor(backgroundColor)
        self.rootWindow.tracer(0)


    def getRootWindow(self):
        return self.rootWindow
    
    def gameListenToPresskey(self, basilisk):
        self.rootWindow.listen()
        self.rootWindow.onkeypress(basilisk.moveUpwards, "Up")
        self.rootWindow.onkeypress(basilisk.moveDownwards, "Down")
        self.rootWindow.onkeypress(basilisk.moveLeftwards, "Left")
        self.rootWindow.onkeypress(basilisk.moveRightwards, "Right")
    
    def gamefieldUpdate(self):
        self.rootWindow.update()
    
    def gamefieldMainloop(self):
        self.rootWindow.mainloop()