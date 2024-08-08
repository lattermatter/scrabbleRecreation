from classes import * 
from data import *

# orientation = input("l for left to right, u for top to bottom: ").strip().lower()
# starting_coordinate = [int(x) for x in input("two space separated numbers for the starting coordinate (0,0  is top left; 14,14 is bottom right): ").split()]
# word = input("enter word: ").upper().split()

orientation, starting_coordinate, word = ["l", [0, 0], "apple"]

board = Board()
board.board_array = addWord(board.board_array, word, orientation, starting_coordinate)
orientation, starting_coordinate, word = ["u", [1, 0], "e"]
board.board_array = addWord(board.board_array, word, orientation, starting_coordinate)

example_turn = [{"a":[0,0], "p":[0,1], "p": [0,2], "l": [0,3], "e": [0,4]}, {"a": [0,0], "e": [1,0]}]
example_turn = [{tuple(k):v for v,k in dict.items()} for dict in example_turn]
print(example_turn)
print(getScore(example_turn))

# total_points += 50 if all tiles played