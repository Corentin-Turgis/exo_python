from Python.packages.cards_game import Board, Player

table1 = Board()
table1.player_join(Player('corentin'))
table1.player_join(Player('flora'))

print(table1)