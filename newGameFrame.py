from tkinter import Frame, Entry, Button, Label
from utils import getFullName

class NewGameFrame(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.main_font = master.main_font
        self.game = master.game



        self.title_label = Label(master=self, font=self.main_font, width=12, text="Spielname")
        self.entry = Entry(master=self, font=self.main_font, width=12, justify="center")
        self.next_button = Button(master=self, font=self.main_font, width=6, text="Weiter", command=self.try_name)
        self.back_button = Button(master=self, font=self.main_font, width=6, text="Zurück", command=self.frame_Home)

        self.title_label.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.entry.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
        self.next_button.grid(row=2, column=0, sticky="nswe", padx=5, pady=5)
        self.back_button.grid(row=3, column=0, sticky="nswe", padx=5, pady=5)

        print(getFullName(self))

    def try_name(self, event=None):
        name = self.entry.get()
        available = self.game.game_name_available(name)
        self.entry["fg"] = "darkred" if not available else "black"

    def frame_Home(self, event=None):
        self.grid_forget()
        self.nametowidget(".!homeframe").grid(row=0, column=0)