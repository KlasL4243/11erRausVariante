from tkinter import Frame, Button
from tkinter.font import Font

class HomeFrame(Frame):
    def __init__(self, master):
        super().__init__(master=master)

        # no expanding

        self.font24 = Font(family="Segoe UI", size=24, weight="bold")

        self.new_game_button = Button(master=self, font=self.font24, width=20, text="Neues Spiel", state="disabled")
        self.resume_button = Button(master=self, font=self.font24, width=20, text="Fortsetzen", state="disabled")
        self.close_button = Button(master=self, font=self.font24, width=20, text="Beenden", command=self.tk.quit)

        self.new_game_button.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.resume_button.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
        self.close_button.grid(row=2, column=0, sticky="nswe", padx=5, pady=5)