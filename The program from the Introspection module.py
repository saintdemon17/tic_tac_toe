from gameparts import Board

game = Board()

print(isinstance(game, Board))
print(isinstance(game, str))

# Выведется:
# True
# False 

print(type(game) is Board)
print(type(game) == Board)
print(type(game) == str)

# Выведется: 
# True
# True
# False