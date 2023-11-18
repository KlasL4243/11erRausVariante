from tkinter import Button

from frames.baseFrame import BaseFrame

class HomeFrame(BaseFrame):
    def __init__(self, master, main_font, game, is_mobile):
        super().__init__(master=master, main_font=main_font, game=game)
        self.is_mobile = is_mobile

        # no expanding

        self.new_game_button = Button(master=self, font=self.main_font, width=12, text="Neues Spiel")
        self.resume_button = Button(master=self, font=self.main_font, width=12, text="Fortsetzen")
        self.close_button = Button(master=self, font=self.main_font, width=12, text="Beenden")

        self.new_game_button["command"] = lambda: self.gridFrame("newgameframe")
        self.resume_button["command"] = lambda: self.gridFrame("resumegameframe")
        self.close_button["command"] = self.quit

        self.new_game_button.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.resume_button.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
        self.close_button.grid(row=2, column=0, sticky="nswe", padx=5, pady=5)