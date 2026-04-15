class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)


game = Board()
game.display()
game.make_move(1, 1, 'X')
print('Ход сделан!')
game.display()




from gameparts import Board


from gameparts.exceptions import FieldIndexError


def main():
    game = Board()
    game.display()
    row = int(input('Введите номер строки: '))
    if row < 0 or row >= game.field_size:
        raise FieldIndexError
    column = int(input('Введите номер столбца: '))
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()

if __name__ == '__main__':
    main()