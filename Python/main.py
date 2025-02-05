from Python.packages.cards_game import Board, Player, Card

table1 = Board()
table1.player_join(Player('Corentin'))
table1.player_join(Player('Flora'))
table1.player_join(Player('Rico'))
table1.player_join(Player('Thibaut'))
table1.player_join(Player('Tao'))

table1.start_game()

for player in table1.players:
    print(f'{player.pseudo} :')
    Card.display_cards(player.hand)