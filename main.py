from tkinter import Tk, Label

from game import Game
from homeFrame import HomeFrame

class App:
    def __init__(self):
        self.tk = Tk()
        self.game = Game()

        self.tk.grid_rowconfigure(index=0, weight=1)
        self.tk.grid_columnconfigure(index=0, weight=1)

        self.width = 1080
        self.height = 2076

        self.tk.update()
        self.is_mobile = self.tk.geometry().startswith(f"{self.width}x{self.height}")

        if not self.is_mobile:
            # halfing size to fit desktop
            self.width //= 2
            self.height //= 2
            # mobile size unchangble anyway
            self.tk.geometry(f'{self.width}x{self.height}+0+0')

        self.home_frame = HomeFrame(master=self.tk)
        self.home_frame.grid(row=0, column=0)



if __name__ == "__main__":
    app = App()

    player_list = ["Lukas", "Mirjam", "Maik", "Selina"]
    app.game.addPlayers(player_list)

    app.tk.mainloop()