import turtle

class Gamefield:
    def __init__(self, title, backgroundColor):
        self.rootWindow = turtle.Screen()
        self.rootWindow.title(title)
        self.rootWindow.bgcolor(backgroundColor)
        self.rootWindow.setup(width = 600 , height = 600) # Erstelle Spielfeld
        self.rootWindow.tracer(0)
    
    def gameListenToPresskey(self, basilisk): # basilisk muss ein Turtle-Element sein
        self.rootWindow.listen()
        self.rootWindow.onkeypress(basilisk.moveUpwards, "Up")
        self.rootWindow.onkeypress(basilisk.moveDownwards, "Down")
        self.rootWindow.onkeypress(basilisk.moveLeftwards, "Left")
        self.rootWindow.onkeypress(basilisk.moveRightwards, "Right")
    
    def gamefieldUpdate(self):
        self.rootWindow.update()
    
    def gamefieldMainloop(self):
        self.rootWindow.mainloop()