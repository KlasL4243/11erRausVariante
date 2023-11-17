from tkinter import Frame, Label

def rotated(list_: list, index_: int) -> list:
    index_ = index_ % len(list_)
    return list_[index_:] + list_[0: index_]

class Fr(Frame):
    def __init__(self, master):
        super().__init__(master=master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.label = Label(master=self, text="Frame")
        self.label.grid(row=0, column=0, sticky="nswe")

class Game:
    def __init__(self, max_cards=7):
        self.max_cards = max_cards
        self.players = {}

        self.order = []
        self.index = 0
        self.sub_order = []
        self.sub_index = 0

        # rounds are range 1 to max to 1
        self.rounds = list(range(1, self.max_cards, 1)) + list(range(max_cards, 0, -1))
        self.round_number = len(self.rounds)

    def addPlayers(self, players: list):
        for player in players:
            self.players[player] = {
                "bets": [-1 * self.round_number],
                "wins": [-1 * self.round_number],
                "scores": [-1 * self.round_number]}

    def set_order(self):
        self.order = rotated(list(self.players.keys()), self.index)

    def set_sub_order(self):
        self.sub_order = rotated(list(self.players.keys()), self.sub_index)

    def get_cards(self) -> int:
        return self.rounds[self.index]