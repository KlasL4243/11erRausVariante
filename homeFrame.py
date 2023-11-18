from tkinter import Frame, Button
from tkinter.font import Font

class HomeFrame(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.is_mobile = master.is_mobile
        print(self.is_mobile)

        # no expanding

        self.font24 = Font(family="Segoe UI", size=24, weight="bold")
        self.button_width = 20

        self.new_game_button = Button(master=self, font=self.font24, width=self.button_width, text="Neues Spiel", state="disabled")
        self.resume_button = Button(master=self, font=self.font24, width=self.button_width, text="Fortsetzen", state="disabled")
        self.close_button = Button(master=self, font=self.font24, width=self.button_width, text="Beenden", command=self.tk.quit)

        self.new_game_button.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.resume_button.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
        self.close_button.grid(row=2, column=0, sticky="nswe", padx=5, pady=5)