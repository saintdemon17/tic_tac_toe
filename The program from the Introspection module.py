# Из модуля inspect импортировать функцию getsource.
from inspect import getsource

from gameparts import Board

game = Board()

# Функция getsource() в работе.
print(getsource(Board))