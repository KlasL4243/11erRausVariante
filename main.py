from tkinter import Tk
from tkinter.font import Font

from frames.homeFrame import HomeFrame
from frames.newGameFrame import NewGameFrame
from frames.resumeGameFrame import ResumeGameFrame
from frames.namesFrame import NamesFrame
from frames.betsFrame import BetsFrame

from game import Game


class App(Tk):
    def __init__(self, game: Game):
        super().__init__()
        self.game = game

        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.width = 1080
        self.height = 2076

        self.is_mobile = self.winfo_screenwidth() == self.width

        if not self.is_mobile:
            # halfing size to fit desktop
            self.width //= 2
            self.height //= 2
            # mobile size unchangble anyway
            self.geometry(f'{self.width}x{self.height}+0+0')
            self.resizable(False, False)

        self.main_font = Font(family="Segoe UI", size=(24 if self.is_mobile else 36), weight="bold")

        self.frame_kwargs = {"master": self, "main_font": self.main_font, "game": self.game}

        self.home_frame = HomeFrame(**self.frame_kwargs, is_mobile=self.is_mobile)
        self.home_frame.grid(row=0, column=0)

        self.new_game_frame = NewGameFrame(**self.frame_kwargs)
        self.resume_game_frame = ResumeGameFrame(**self.frame_kwargs)
        self.names_frame = NamesFrame(**self.frame_kwargs)
        self.bets_frame = BetsFrame(**self.frame_kwargs)





if __name__ == "__main__":
    from cProfile import Profile
    from pstats import Stats, SortKey

    with Profile() as pr:
        game = Game()
        app = App(game=game)

        app.tk.mainloop()
        game.save()

    stats = Stats(pr)
    stats.sort_stats(SortKey.TIME)
    stats.print_stats()