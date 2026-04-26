from gameparts import Board

game = Board()

print(game.__class__.__dict__)

# Выведется:
# {'__module__': 'gameparts.parts', '__init__': <function Board.__init__ at 0x104f95f70>, 'make_move': <function Board.make_move at 0x104fa3040>, 'display': <function Board.display at 0x104fa30d0>, '__dict__': <attribute '__dict__' of 'Board' objects>, '__weakref__': <attribute '__weakref__' of 'Board' objects>, '__doc__': None} 

print(type(game) is Board)
print(type(game) == Board)
print(type(game) == str)

# Выведется: 
# True
# True
# False