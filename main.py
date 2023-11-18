from customtkinter import CTk

from game import Game
from homeFrame import HomeFrame

class App(CTk):
    def __init__(self):
        super().__init__()

        self.game = Game()

        self.grid_rowconfigure(index=0, weight=1)
        self.grid_columnconfigure(index=0, weight=1)

        self.width = 1080
        self.height = 2076

        self.update()
        self.is_mobile = self.geometry().startswith(f"{self.width}x{self.height}")

        if not self.is_mobile:
            # halfing size to fit desktop
            self.width //= 2
            self.height //= 2
            # mobile size unchangble anyway
            self.geometry(f'{self.width}x{self.height}+0+0')

        self.home_frame = HomeFrame(master=self)
        self.home_frame.grid(row=0, column=0)



if __name__ == "__main__":
    app = App()

    player_list = ["Lukas", "Mirjam", "Maik", "Selina"]
    app.game.addPlayers(player_list)

    app.tk.mainloop()