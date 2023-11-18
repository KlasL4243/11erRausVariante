from tkinter import Frame
from tkinter.font import Font

from game import Game


class BaseFrame(Frame):
    def __init__(self, master, main_font: Font, game: Game):
        super().__init__(master=master)
        self.main_font = main_font
        self.game = game

    def gridFrame(self, name: str):
        self.grid_forget()
        self.nametowidget(f".!{name}").grid(row=0, column=0)