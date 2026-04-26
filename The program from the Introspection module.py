from gameparts import Board

game = Board()

print('__str__' in dir(game))

# Выведется:
# True

print(type(game) is Board)
print(type(game) == Board)
print(type(game) == str)

# Выведется: 
# True
# True
# False