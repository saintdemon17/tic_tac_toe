from gameparts import Board

game = Board()
print(game.__class__)

# Выведется: 
# <class 'gameparts.parts.Board'>

print(type(game) is Board)
print(type(game) == Board)
print(type(game) == str)

# Выведется: 
# True
# True
# False