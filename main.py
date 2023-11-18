from tkinter import Tk
from tkinter.font import Font

from game import Game
from frames.homeFrame import HomeFrame
from frames.newGameFrame import NewGameFrame
from frames.resumeGameFrame import ResumeGameFrame

class App(Tk):
    def __init__(self):
        super().__init__()

        self.game = Game()

        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.width = 1080
        self.height = 2076

        self.is_mobile = self.winfo_screenwidth() == str(self.width)

        if not self.is_mobile:
            # halfing size to fit desktop
            self.width //= 2
            self.height //= 2
            # mobile size unchangble anyway
            self.geometry(f'{self.width}x{self.height}+0+0')
            self.resizable(False, False)

        self.main_font = Font(family="Segoe UI", size=(24 if self.is_mobile else 36), weight="bold")

        self.home_frame = HomeFrame(master=self)
        self.new_game_frame = NewGameFrame(master=self)
        self.resume_game_frame = ResumeGameFrame(master=self)


        self.home_frame.grid(row=0, column=0)



if __name__ == "__main__":
    app = App()

    player_list = ["Lukas", "Mirjam", "Maik", "Selina"]
    app.game.addPlayers(player_list)

    app.tk.mainloop()