import tkinter as tk
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.game = Game()


class Game:
    def __init__(self):
        print("game initialised")


if __name__ == "__main__":
    app = App()

    app.mainloop()