import turtle

class Gamefield:
    def __init__(self, title, backgroundColor):
        self.rootWindow = turtle.Screen()
        self.rootWindow.title(title)
        self.rootWindow.bgcolor(backgroundColor)
        self.rootWindow.setup(width = 600 , height = 600) # Erstelle Spielfeld
        self.rootWindow.tracer(0)