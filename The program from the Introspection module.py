# Из модуля inspect импортировать функцию isfunction.
from inspect import isfunction

from gameparts import Board

game = Board()

# display() - это функция?
print(isfunction(game.display))

# Выведется:
# False 