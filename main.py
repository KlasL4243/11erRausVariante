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

        self.screen_width = self.tk.winfo_screenwidth()
        self.screen_height = self.tk.winfo_screenheight()

        if self.height != self.screen_height:  # halfing size for desktop
            self.width //= 2
            self.height //= 2

        self.tk.geometry(f'{self.width}x{self.height}+0+0')
        self.home_frame = HomeFrame(master=self.tk)
        self.home_frame.grid(row=0, column=0)


if __name__ == "__main__":
    app = App()

    player_list = ["Lukas", "Mirjam", "Maik", "Selina"]
    app.game.addPlayers(player_list)

    app.tk.mainloop()