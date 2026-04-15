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
    current_player = 'X'
    running = True
    game.display()
    while running:

        print(f'Ход делают {current_player}')
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    game.display()
    current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()