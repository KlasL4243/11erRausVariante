from tkinter import Tk, Label

from game import Game
from homeFrame import HomeFrame

class App:
    def __init__(self):
        self.tk = Tk()
        self.game = Game()

        self.tk.grid_rowconfigure(index=0, weight=1)
        self.tk.grid_columnconfigure(index=0, weight=1)

        print(self.tk.geometry())

        self.width = 1080//2
        self.height = 2076//2

        self.screen_width = self.tk.winfo_screenwidth()
        self.screen_height = self.tk.winfo_screenheight()

        self.tk.geometry(f'{self.width}x{self.height}')
        self.home_frame = HomeFrame(master=self.tk)
        self.home_frame.grid(row=0, column=0)

        print(self.tk.geometry())


if __name__ == "__main__":
    app = App()

    player_list = ["Lukas", "Mirjam", "Maik", "Selina"]
    app.game.addPlayers(player_list)

    app.tk.mainloop()