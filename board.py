from classes import * 
from data import *

# orientation = input("l for left to right, u for top to bottom: ").strip().lower()
# starting_coordinate = [int(x) for x in input("two space separated numbers for the starting coordinate (0,0  is top left; 14,14 is bottom right): ").split()]
# word = input("enter word: ").upper().split()


board = Board()
board.board_array = addWord(board.board_array, "homunculus", "u", [0,1])
board.board_array = addWord(board.board_array, "hermen", "l", [0,1])
print(board)

create = createWord("u", [0,1], board.board_array)
score = getScore([create], board)
print(score)

# example_turn = [{"a":[0,0], "p":[0,1], "p": [0,2], "l": [0,3], "e": [0,4]}, {"a": [0,0], "e": [1,0]}]
# example_turn = [{tuple(k):v for v,k in dict.items()} for dict in example_turn]
# print(example_turn)
# print(getScore(example_turn))

# total_points += 50 if all tiles played

