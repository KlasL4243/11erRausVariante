from tkinter import Entry, Button, Label
from frames.baseFrame import BaseFrame

class NewGameFrame(BaseFrame):
    def __init__(self, master, main_font, game):
        super().__init__(master=master, main_font=main_font, game=game)

        self.title_label = Label(master=self, font=self.main_font, width=12, text="Spielname")
        self.entry = Entry(master=self, font=self.main_font, width=12, justify="center")
        self.next_button = Button(master=self, font=self.main_font, width=12, text="Weiter")
        self.back_button = Button(master=self, font=self.main_font, width=12, text="Zurück")

        self.entry.insert(0, "Spiel01")
        self.next_button["command"] = self.try_name
        self.back_button["command"] = lambda: self.gridFrame("homeframe")


        self.title_label.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.entry.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
        self.next_button.grid(row=2, column=0, sticky="nswe", padx=5, pady=5)
        self.back_button.grid(row=3, column=0, sticky="nswe", padx=5, pady=5)


    def try_name(self, event=None):
        game_name = self.entry.get()
        available = self.game.available(name=game_name)
        self.entry["fg"] = "darkred" if not available else "black"

        if available:
            self.game.game_name = game_name
            self.gridFrame("namesframe")