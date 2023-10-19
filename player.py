class Player:
    def __init__(self, num, mark):
        self.num = num
        self.mark = mark

    def __str__(self):
        return f'Player {self.num} ({self.mark})'
