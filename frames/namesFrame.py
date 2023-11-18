from tkinter import Label, Button, Text

from frames.baseFrame import BaseFrame


class NamesFrame(BaseFrame):
    def __init__(self, master, main_font, game):
        super().__init__(master=master, main_font=main_font, game=game)

        self.title_label = Label(master=self, font=self.main_font, width=12, text="Spielernamen")
        self.multi_text = Text(master=self, font=self.main_font, width=12, height=10)
        self.next_button = Button(master=self, font=self.main_font, width=12, text="Weiter")
        self.back_button = Button(master=self, font=self.main_font, width=12, text="Zurück")
        self.next_button["command"] = self.startGame
        self.back_button["command"] = lambda: self.gridFrame("newgameframe")


        self.title_label.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.multi_text.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
        self.next_button.grid(row=2, column=0, sticky="nswe", padx=5, pady=5)
        self.back_button.grid(row=3, column=0, sticky="nswe", padx=5, pady=5)

    def startGame(self):
        names = [name.strip() for name in self.multi_text.get("0.0", "end").split("\n") if name.strip()]
        if len(names) < 5:  # not enough Players
            return

        self.game.addPlayers(players=names)
        self.gridFrame("betsframe")


