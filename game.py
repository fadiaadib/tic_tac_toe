import os
import random
from player import Player

WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
KEYS = {1: 6, 2: 7, 3: 8, 4: 3, 5: 4, 6: 5, 7: 0, 8: 1, 9: 2}


class Game:
    def __init__(self, auto=False):
        self.players = [Player(num=1, mark='X'), Player(num=2, mark='O')]
        self.board = [' ' for _ in range(0, 9)]
        self.cur = 0
        self.first_player_choice()
        self.display_board()
        self.auto = auto

    def first_player_choice(self):
        while True:
            choice = input(f'Player {self.players[0].num}, '
                           f'choose "X" or "O": ').upper()
            if choice in ['X', 'O']:
                if choice == 'O':
                    self.players[0].mark = 'O'
                    self.players[1].mark = 'X'
                break
            else:
                print('Invalid choice, please try again!')

    def check_win(self):
        for a, b, c in WINS:
            if self.board[a] != ' ' and self.board[a] == self.board[b] == self.board[c]:
                print(f'{self.players[self.cur]} wins!')
                return True
        if ' ' not in self.board:
            print('It\'s a draw! Better luck next time...')
            return True

        self.switch_player()
        return False

    def display_board(self):
        os.system('clear')
        for i in range(0, 7, 3):
            print(' ' + ' | '.join(self.board[i:i + 3]))
            if i < 6:
                print('-' * 11)

    def switch_player(self):
        if self.cur == 0:
            self.cur = 1
        else:
            self.cur = 0

    def make_move(self):
        if self.cur == 1 and self.auto:
            while True:
                choice = random.randint(0, 8)
                if self.board[choice] == ' ':
                    self.board[choice] = self.players[self.cur].mark
                    break
        else:
            while True:
                try:
                    choice = int(input(f'{self.players[self.cur]}: Choose a spot (1-9): '))
                    if choice in range(1, 10):
                        if self.board[KEYS[choice]] == ' ':
                            self.board[KEYS[choice]] = self.players[self.cur].mark
                            break
                        else:
                            print('This spot is already filled, try again!')
                    else:
                        raise ValueError
                except ValueError:
                    print('Invalid choice, please try again!')
