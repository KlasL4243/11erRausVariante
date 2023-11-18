from tkinter import Button, Label
from tkinter.ttk import Combobox
from frames.baseFrame import BaseFrame

class ResumeGameFrame(BaseFrame):
    def __init__(self, master, main_font, game):
        super().__init__(master=master, main_font=main_font, game=game)

        self.label = Label(master=self, font=self.main_font, width=12, text="Spielstände")
        self.box = Combobox(master=self, font=self.main_font, width=12, values=self.game.saves_list(), state="readonly")
        self.option_add("*TCombobox*Listbox*Font", self.main_font)

        self.next_button = Button(master=self, font=self.main_font, width=12, text="Weiter", state="disabled")
        self.back_button = Button(master=self, font=self.main_font, width=12, text="Zurück")
        self.next_button["command"] = self.resume_game
        self.back_button["command"] = lambda: self.gridFrame("homeframe")

        self.label.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.box.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
        self.next_button.grid(row=2, column=0, sticky="nswe", padx=5, pady=5)
        self.back_button.grid(row=3, column=0, sticky="nswe", padx=5, pady=5)

    def resume_game(self, event=None):
        name = self.box.get()
        if not self.game.available(name):
            self.game.load(name)