# Из модуля inspect импортировать функцию ismethod.
from inspect import ismethod

from gameparts import Board

game = Board()

# display() - это функция?
print(ismethod(game.display))

#  Вывод: True