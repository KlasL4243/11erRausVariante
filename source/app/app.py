from tkinter import Tk
from source.game import Game
from source.app.frames.homeFrame import HomeFrame

class App(Tk):
    def __init__(self):
        super().__init__()

        window_width = 800
        window_height = 500

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        print(screen_height, screen_width)

        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        self.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=0, weight=1)

        self.game = Game()
        self.home_frame = HomeFrame(master=self)

        self.home_frame.grid(row=0, column=0, sticky="nesw")
