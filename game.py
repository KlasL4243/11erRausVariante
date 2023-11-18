from pandas import DataFrame, read_csv
from glob import glob

class Game:
    def __init__(self, max_cards=7):
        self.max_cards = max_cards
        self.df = None
        self.game_name = ""
        self.players = []

        self.order = []
        self.index = 0
        self.sub_order = []
        self.sub_index = 0

        # rounds are range 1 to max to 1
        self.rounds = list(range(1, self.max_cards, 1)) + list(range(self.max_cards, 0, -1))
        self.round_number = len(self.rounds)


    def save(self):
        if self.df is not None:
            self.df.to_csv(f"saves/save_{self.game_name}.csv", index=False)
            print(f"save_{self.game_name}.csv saved!")
            return
        print("nothing to save!")

    def load(self, name):
        self.game_name = name
        self.df = read_csv(f"saves/save_{name}.csv")
        self.players = list(set(self.df["player"]))
        print(f"save_{name}.csv loaded!")

    def available(self, name: str) -> bool:
        return name not in self.saves_list()

    @staticmethod
    def saves_list() -> list[str]:
        return [save.split("save_")[1].split(".")[0] for save in glob("saves/*.csv")]

    @staticmethod
    def rotated(list_: list, index_: int) -> list:
        index_ = index_ % len(list_)
        return list_[index_:] + list_[0: index_]

    def addPlayers(self, players: list):
        data_list = [[player, index, cards, 0, 0, 0] for player in players for index, cards in enumerate(self.rounds)]

        self.df = DataFrame(data=data_list, columns=["player", "index", "cards", "bet", "wins", "score"])
        self.players = players
        self.save()

    def set_order(self):
        self.order = self.rotated(list(self.players), self.index)

    def set_sub_order(self):
        self.sub_order = self.rotated(list(self.players), self.sub_index)

    def get_cards(self) -> int:
        return self.rounds[self.index]