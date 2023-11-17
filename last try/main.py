from source.app.app import App

if __name__ == "__main__":
    player_list = ["Lukas", "Mirjam", "Maik", "Selina"]

    app = App()
    app.game.addPlayers(player_list)

    app.mainloop()