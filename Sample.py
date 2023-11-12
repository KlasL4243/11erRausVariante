from tkinter import Tk, Label, Button, Entry, Spinbox, font, END

class ElferRaus:
    def __init__(self, maxcards=7, startround=0, winscore=10, losescore=-5, maxplayers=10):
        self._PlayerData = []
        self.WinScore = winscore
        self.Losescore = losescore
        self.MaxPlayers = maxplayers
        self._Round = startround
        self._CardAmount = list(range(1, maxcards)) + list(range(maxcards, 1-1, -1))
        self._MaxRound = maxcards*2-1 # range(maxcards) +range(maxcards-1)

    #def getPlayerNames(self):
    #    return [player["name"] for player in self._PlayerData]

    def getPlayerNumber(self):
        return len(self._PlayerData)

    def _getPlayer(self, playername):
        for player in self._PlayerData:
            if player["name"] == playername: return player
        else: raise AttributeError(f'Player "{playername}" not found !')

    def getPlayerOrder(self):
        first = self._Round % len(self._PlayerData)
        OrderedPlayers = self._PlayerData[first:] + self._PlayerData[0:first]
        return [p["name"] for p in OrderedPlayers]

    def addPlayer(self, name: str, score=0, bet=0, wins=0):
        self._PlayerData.append({"name": name, "score": score, "bet": bet, "wins": wins})

    def setBet(self, playername: str, bet: int):
        self._getPlayer(playername).update({"bet": bet})

    def setWins(self, playername: str, wins: int):
        self._getPlayer(playername).update({"wins": wins})

    def _setScore(self, player: dict):
        score = player["score"] + player["wins"]
        if player.get("bet") == player.get("wins"):
            score += self.WinScore
        else:
            score += self.Losescore
        player.update({"score": score, "bet": 0, "wins": 0})

    def setScores(self):
        for player in self._PlayerData:
            self._setScore(player)

    def getSortedScores(self):
        Scores = sorted(self._PlayerData, key=lambda player: player["score"], reverse=True)
        [player.pop("bet", "wins") for player in Scores]
        return Scores

    def getCurrentCardAmount(self):
        return self._CardAmount[self._Round]

    def addRound(self):
        self._Round += 1

    def isLastRound(self):
        return True if self._Round == self._MaxRound else False


class TkinterApp:
    def __init__(self):
        self._game = ElferRaus()
        self.tk = Tk()
        self.tk.resizable = (False, False)

        self.Comic = font.Font(font=("Comic Sans MS", 30))
        self.Entrys = [Entry(master=self.tk, font=self.Comic) for _ in range(self._game.MaxPlayers)]
        self.Labels = [Label(master=self.tk, relief="raised", font=self.Comic, padx=10) for _ in range(
            self._game.MaxPlayers)]
        self.nextButton = Button(master=self.tk, text="Weiter", font=self.Comic)
        self.titleLabel = Label(master=self.tk, font=self.Comic, justify="center")
        self.Spinboxes = []

        self.displayScreen_Names()
        self.tk.mainloop()


    def displayScreen_Names(self): # GUI für Spielernamen-Eingabe
        for widget in self.tk.winfo_children(): widget.grid_forget()

        self.titleLabel.config(text="Spielernamen")
        self.titleLabel.pack()
        for e in self.Entrys: e.pack(padx=1, pady=1)
        self.nextButton.config(command=self.setPlayerNames)
        self.nextButton.pack()

    def setPlayerNames(self): # Speichert eingegebene Spielernamen
        for entry in self.Entrys:
            if entry.get() != "":
                self._game.addPlayer(name=entry.get())
            entry.destroy()
        self.Spinboxes = [Spinbox(font=self.Comic, justify="center", width=3) for _ in range(
            self._game.getPlayerNumber())]
        self.displayScreen_Tips()

    def displayScreen_Tips(self):
        for widget in self.tk.winfo_children(): widget.pack_forget()
        [spinbox.delete(0, END) for spinbox in self.Spinboxes]

        self.titleLabel.config(text=f"Tipps (0-{self._game.getCurrentCardAmount()}):")
        self.titleLabel.grid(row=0, column=0, columnspan=2)

        for index, playername in enumerate(self._game.getPlayerOrder()):
            self.Labels[index].config(text=playername)
            self.Labels[index].grid(row=index + 1, column=0, padx=1, pady=1, sticky="we")

            self.Spinboxes[index].config(from_=0, to_=self._game.getCurrentCardAmount())
            self.Spinboxes[index].delete(0, END)
            self.Spinboxes[index].grid(row=index + 1, column=1, padx=1, sticky="we")

        self.nextButton.config(command=self.setTips)
        self.nextButton.grid(row=self._game.getPlayerNumber() + 1, column=0, columnspan=2)

    def setTips(self):
        tips = [spinbox.get() for spinbox in self.Spinboxes]
        if "" in tips: return

        for index, tip in enumerate(tips):
            self._game.setBet(self.Labels[index]["text"], int(tip))
        self.displayScreen_Wins()

    def displayScreen_Wins(self):
        [spinbox.delete(0, END) for spinbox in self.Spinboxes]
        self.titleLabel.config(text=f"Gewinne ({self._game.getCurrentCardAmount()}):")
        self.nextButton.config(command=self.setWins)

    def setWins(self):
        wins = []
        for spinbox in self.Spinboxes:
            if spinbox.get() == "": return
            wins.append(int(spinbox.get()))

        winSum = sum(wins)
        if winSum != self._game.getCurrentCardAmount():
            self.titleLabel.config(text=f"Gewinne ({winSum}/{self._game.getCurrentCardAmount()}):")
            return

        for index, wins in enumerate(wins):
            self._game.setWins(self.Labels[index]["text"], int(wins))
        self.displayScreen_Scores()

    def displayScreen_Scores(self):
        self._game.setScores()
        for widget in self.tk.winfo_children(): widget.grid_forget()

        if self._game.isLastRound():
            self.titleLabel.config(text="Finaler Punktestand:")
            self.nextButton.config(text="Exit", command=self.tk.quit)
            return
        else:
            self.titleLabel.config(text="Punktestand:")
            self.nextButton.config(command=self.Reset)

        self.titleLabel.pack()

        for index, player in enumerate(self._game.getSortedScores()):
            self.Labels[index].config(text=f'{player["name"]}: {player["score"]}')
            self.Labels[index].pack()


        self.nextButton.pack()
    def Reset(self):
        self._game.addRound()
        self.displayScreen_Tips()

if __name__ == "__main__":
    TkinterApp()
