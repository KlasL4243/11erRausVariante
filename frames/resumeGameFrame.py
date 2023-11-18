from tkinter import Frame, Entry, Button, Label
from tkinter.ttk import Combobox
from utils import getFullName

class ResumeGameFrame(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.main_font = master.main_font
        self.game = master.game

        self.label = Label(master=self, font=self.main_font, width=12, text="Spielstände")
        self.box = Combobox(master=self, font=self.main_font, width=12, values=self.game.saves_list(), state="readonly")
        self.option_add("*TCombobox*Listbox*Font", self.main_font)

        self.next_button = Button(master=self, font=self.main_font, width=12, text="Weiter", command=self.resume_game)
        self.back_button = Button(master=self, font=self.main_font, width=12, text="Zurück", command=self.frame_Home)

        self.label.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.box.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
        self.next_button.grid(row=2, column=0, sticky="nswe", padx=5, pady=5)
        self.back_button.grid(row=3, column=0, sticky="nswe", padx=5, pady=5)

    def resume_game(self, event=None):
        name = self.box.get()
        print(name)

    def frame_Home(self, event=None):
        self.grid_forget()
        self.nametowidget(".!homeframe").grid(row=0, column=0)