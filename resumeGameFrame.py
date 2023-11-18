from tkinter import Frame, Entry, Button, Label
from utils import getFullName

class NewGameFrame(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.main_font = master.main_font
        self.game = master.game

