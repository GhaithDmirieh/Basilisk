from tkinter import *

class MainMenu:
    def __init__(self):
        
        self.root = Tk()

        self.background_highscore_label = Label(self.root, text = "Highscore im Hintergrund", padx = 10, pady = 5, width = 20)
        self.headline_label = Label(self.root, text = "Welcome to Basilisk", padx = 10, pady = 5, width = 20)
        

        self.start_game_button = Button(self.root, text = "Start Game", padx = 10, pady = 5, command = self.start_game_button_command)
        self.load_game_button = Button(self.root, text = "Load Game", padx = 10, pady = 5, command = self.load_game_button_command)

        self.background_highscore_label.pack()
        self.headline_label.pack()
        self.start_game_button.pack()
        self.load_game_button.pack()
        self.root.mainloop()

    def start_game_button_command(self):
        pass #todo


    def load_game_button_command(self):
        pass #todo 

    

# _________________________________________________________________________________________________________________________________

root = Tk()
root.title("Basilisk - The Game")
root.geometry("600x600")

g = IntVar()
g.set(1)

s1 = IntVar()
s2 = IntVar()
s3 = IntVar()
s4 = IntVar()
s5 = IntVar()
s6 = IntVar()

headline_label = Label(root, text = "Welcome to Basilisk")
background_highscore_label = Label(root, text = "Highscore im Hintergrund")
alternative_gamemode_label= Label(root, text = "Alternative Spielmodi")
other_settings_label= Label(root, text = "Sonstige Einstellungen")

start_game_button = Button(root, text = "Start Game")
load_game_button = Button(root, text = "Load Game")

gamemode1 = Radiobutton(root, text = "Gamemode 1", variable = g, value=1)
gamemode2 = Radiobutton(root, text = "Gamemode 2", variable = g, value=2)
gamemode3 = Radiobutton(root, text = "Gamemode 3", variable = g, value=3)
gamemode4 = Radiobutton(root, text = "Gamemode 4", variable = g, value=4)
gamemode5 = Radiobutton(root, text = "Gamemode 5", variable = g, value=5)
gamemode6 = Radiobutton(root, text = "Gamemode 6", variable = g, value=6)

setting1 = Checkbutton(root, text = "Setting 1", variable = s1)
setting2 = Checkbutton(root, text = "Setting 2", variable = s2)
setting3 = Checkbutton(root, text = "Setting 3", variable = s3)
setting4 = Checkbutton(root, text = "Setting 4", variable = s4)
setting5 = Checkbutton(root, text = "Setting 5", variable = s5)
setting6 = Checkbutton(root, text = "Setting 6", variable = s6)

headline_label.grid(row=0, column=1)
background_highscore_label.grid(row=1, column=1)
start_game_button.grid(row=2, column=1)
load_game_button.grid(row=3, column=1)
alternative_gamemode_label.grid(row=4, column=1)
gamemode1.grid(row=5,column=0)
gamemode2.grid(row=5,column=1)
gamemode3.grid(row=5,column=2)
gamemode4.grid(row=6,column=0)
gamemode5.grid(row=6,column=1)
gamemode6.grid(row=6,column=2)
other_settings_label.grid(row=7, column=1)
setting1.grid(row=8,column=0)
setting2.grid(row=8,column=1)
setting3.grid(row=8,column=2)
setting4.grid(row=9,column=0)
setting5.grid(row=9,column=1)
setting6.grid(row=9,column=2)

root.mainloop()