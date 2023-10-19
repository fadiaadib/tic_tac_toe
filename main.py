from game import Game
from banner import banner

print(banner)
game = Game(auto=input('Choose number of players (1) or (2): ') != '2')
while True:
    game.make_move()
    game.display_board()
    if game.check_win():
        break
