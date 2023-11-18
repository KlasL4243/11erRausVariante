from tkinter import Label, Button

from frames.baseFrame import BaseFrame

class BetsFrame(BaseFrame):
    def __init__(self, master, main_font, game):
        print("p")
        super().__init__(master=master, main_font=main_font, game=game)
        self.buttons = []

        self.title_label = Label(master=self, font=self.main_font, width=12)
        self.title_label["text"] = f"Wetten (0-{self.game.get_cards()})"

        self.next_button = Button(master=self, font=self.main_font, width=12, text="Weiter")
        self.back_button = Button(master=self, font=self.main_font, width=12, text="Zurück")
        self.next_button["command"] = None
        self.back_button["command"] = lambda: self.gridFrame("homeframe")


        self.title_label.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)

    def setButtons(self):
        self.buttons = [Button(master=self, font=self.main_font, width=12, text=f"{player} ( -1 )") for player in self.game.players]
        print()
        for index, button in enumerate(self.buttons + [self.next_button, self.back_button], start=3):
            button.grid(row=index, column=0, sticky="nswe", padx=5, pady=5)

    def grid(self, **kwargs):
        self.setButtons()
        super().grid(**kwargs)