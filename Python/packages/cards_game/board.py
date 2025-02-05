from .deck import Deck
from .player import Player


class Board:
    def __init__(self):
        self.deck: Deck = Deck()
        self.players: list[Player] = []

    def player_join(self, player: Player):
        self.players.append(player)

    # def player_quit(self, player: Player):
    #     if player in self.players:
    #         for card in player.hand:
    #             self.deck

            # self.players.remove(player)

    def __repr__(self):
        return f'Board(Players: {[player.pseudo for player in self.players]}, Deck: {len(self.deck)} cards remaining'