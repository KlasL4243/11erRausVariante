from json import load, dump


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

        # load games
        with open("data.json", mode='r', encoding="utf-8") as file:
            self.data = load(file)

    def game_name_available(self, name: str) -> bool:
        return name not in self.data.keys()

    @staticmethod
    def rotated(list_: list, index_: int) -> list:
        index_ = index_ % len(list_)
        return list_[index_:] + list_[0: index_]

    def addPlayers(self, players: list):
        for player in players:
            self.players[player] = {
                "bets": [-1 * self.round_number],
                "wins": [-1 * self.round_number],
                "scores": [-1 * self.round_number]}

    def set_order(self):
        self.order = self.rotated(list(self.players.keys()), self.index)

    def set_sub_order(self):
        self.sub_order = self.rotated(list(self.players.keys()), self.sub_index)

    def get_cards(self) -> int:
        return self.rounds[self.index]