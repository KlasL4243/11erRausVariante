import customtkinter as ctk

class HomeFrame(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master=master)

        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=1, weight=1)

        self.font24 = ctk.CTkFont(family="Segoe UI", size=24, weight="bold")

        self.new_game_button = ctk.CTkButton(master=self, font=self.font24, width=20, text="Neues Spiel")
        self.resume_button = ctk.CTkButton(master=self, font=self.font24, width=20, text="Fortsetzen")

        self.new_game_button.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.resume_button.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)