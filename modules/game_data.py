# game_data.py
import pickle


class GameData:
    def __init__(self, filename='savegame.pkl'):
        self.filename = filename

    def save(self, game):
        with open(self.filename, 'wb') as file:
            pickle.dump(game, file)
        print("Game data saved successfully.")

    def load(self):
        try:
            with open(self.filename, 'rb') as file:
                game = pickle.load(file)
            print("Game data loaded successfully.")
            return game
        except FileNotFoundError:
            print("No saved game found.")
            return None
