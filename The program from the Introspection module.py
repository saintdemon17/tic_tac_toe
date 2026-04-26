from gameparts import Board

game = Board()

print(hasattr(game, '__str__'))

# Выведется:
# True

print(type(game) is Board)
print(type(game) == Board)
print(type(game) == str)

# Выведется: 
# True
# True
# False