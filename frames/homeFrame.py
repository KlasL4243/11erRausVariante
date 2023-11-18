from tkinter import Frame, Button

class HomeFrame(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.is_mobile = master.is_mobile
        self.main_font = master.main_font

        # no expanding

        self.button_kwargs = {"master": self, "font": self.main_font, "width": 12}

        self.new_game_button = Button(**self.button_kwargs, text="Neues Spiel", command=self.frame_newGame)
        self.resume_button = Button(**self.button_kwargs, text="Fortsetzen", command=self.frame_resumeGame)
        self.close_button = Button(**self.button_kwargs, text="Beenden", command=self.tk.quit)

        self.new_game_button.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.resume_button.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
        self.close_button.grid(row=2, column=0, sticky="nswe", padx=5, pady=5)

    def frame_newGame(self, event=None):
        self.grid_forget()
        self.nametowidget(".!newgameframe").grid(row=0, column=0)

    def frame_resumeGame(self, event=None):
        self.grid_forget()
        self.nametowidget(".!resumegameframe").grid(row=0, column=0)