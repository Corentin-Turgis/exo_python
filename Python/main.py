from Python.packages.cards_game import Board, Player

table1 = Board()
table1.player_join(Player('corentin'))
table1.player_join(Player('flora'))

table1.player_draw(table1.players[0])
table1.player_draw(table1.players[0])