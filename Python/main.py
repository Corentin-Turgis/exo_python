from Python.packages.cards_game import Board, Player, Card

tao = Player('Tao')

table1 = Board()
table1.player_join(Player('Corentin'))
table1.player_join(Player('Flora'))
table1.player_join(Player('Rico'))
table1.player_join(Player('Thibaut'))
table1.player_join(tao)

table1.start_game()