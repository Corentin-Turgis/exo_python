import random

from .exceptions import DuplicateUserException
from .deck import Deck
from .player import Player


class Board:
    def __init__(self):
        self.deck: Deck = Deck()
        self.players: list[Player] = []

    def player_join(self, player: Player):
        if player in self.players:
            raise DuplicateUserException
        self.players.append(player)
        print(f'{player} join the table')

    def player_quit(self, player: Player):
        if player in self.players:
            for card in player.hand:
                self.deck.add_card(card)
        self.players.remove(player)
        print(f'{player} quit the table')

    def player_draw(self, player):
        if len(self.deck.cards) <= 0:
            print(f'Sorry {player.pseudo} ! No more cards in this deck :(')
            return
        card = self.deck.draw()
        player.add_card_to_hand(card)
        print(f'{player} draw a card from {self.deck}')

    def start_game(self):
        players_nb = len(self.players)
        parts = self.deck.deal_deck(players_nb)
        random.shuffle(self.players)
        i = 0
        while i < players_nb:
            self.players[i].hand = parts[i]
            i += 1

    def __repr__(self):
        return f'Board(Players: {[player.pseudo for player in self.players]}, {self.deck}'
