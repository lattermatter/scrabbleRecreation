from data import *

class Cell():
    def __init__(self, row, col, connections=set(), val=""):
        self.row = row
        self.col = col
        self.val = val
        self.connections = connections
        self.ID = 0
        for ID, powerup in powerupDict.items():
            if [self.row, self.col] in powerup:
                self.ID = ID
                break
            
    def deactivateCell(self):
        self.ID = 0
        return self.ID
    
    def changeVal(self, val):
        self.val = val
            
            
class Board(Cell):
    def __init__(self):
        board_array = [[Cell(i, j) for i in range(0, 15)] for j in range(0, 15)]
        self.board_array = board_array
        
    def get(self, row, col):
        return self.board_array[row][col].val
    
    def array(self):
        return [[self.board_array[row][col].val for row in range(0, 15)] for col in range(0, 15)]
    
    def __str__(self):
        
        str_return = displayColNumbers()
        for row in range(boardLength):
            str_return += displayRowNumbers(row)
            for col in range(boardLength):
                current_val = self.board_array[row][col].val
                if current_val: 
                    str_return += f" {current_val} |"
                    continue
                str_return += f"   |" 
                
            str_return += "\n\n"
        return str_return
    
    def map(self):
        str_return = ''
        for row in range(boardLength):
            str_return += "|"
            for col in range(boardLength):
                if [row,col] in DoubleLetter:
                        str_return += " d |"
                elif [row,col] in DoubleWord:
                    str_return += " D |"
                elif [row,col] in TripleLetter:
                    str_return += " t |"
                elif [row,col] in TripleWord:
                    str_return += " T |"
                else:
                    str_return += "   |"
            str_return += "\n\n"
        return str_return

class ScrabbleError(Exception):
    def __init__(self, message, *args, **kwargs) -> None:
        self.message = message
        print(message)
        super().__init__(*args, **kwargs)

# unfinished
def addWord(board, word, direction, position):
    try:
        # use connections to determine how words can be linked
        if direction == "l":
            for index in range(len(word)):
                # check if there is an existing letter in the sections
                board[position[0]][position[1] + index].val = word[index]
                if index == 0:
                    board[position[0]][position[1] + index].connections.update([1])
                elif index == len(word) - 1:
                    board[position[0]][position[1] + index].connections.update([3])
                else:
                    board[position[0]][position[1] + index].connections.update([1,3])
        elif direction == "u":
            for index in range(len(word)):
                board[position[0] + index][position[1]].val = word[index]
                if index == 0:
                    board[position[0] + index][position[1]].connections.update([0])
                elif index == len(word) - 1:
                    board[position[0] + index][position[1]].connections.update([2])
                else:
                    board[position[0] + index][position[1]].connections.update([0,2])
        else:
            raise ScrabbleError("Direction incorrect")
        # return [{(x, y): letter,...}, {word2}, {word3}...]
        return board
    except IndexError:
        raise ScrabbleError("Word entered reaches out of bounds")
    
    
def createWord(direction, position, board_array):
    pointer = position.copy()
    final_word_dict = {tuple(pointer): board_array[pointer[0]][pointer[1]].val}
    
    if direction == "l":
        direction = -1
        
        while board_array[pointer[0]][pointer[1]].val != "" and (
            (0 <= pointer[0] and pointer[0] <= 14) and
            (0 <= pointer[1] and pointer[1] <= 14)
        ):
            if pointer[1] + 1*direction < 0:
                break
            next_char = board_array[pointer[0]][pointer[1] + 1*direction].val
            pointer = [pointer[0], pointer[1] + 1*direction]
            final_word_dict = {**{tuple(pointer): next_char}, **final_word_dict} if next_char != "" else final_word_dict
            
        direction = 1
        pointer = position.copy()
        
        while board_array[pointer[0]][pointer[1]].val != "" and (
            (0 <= pointer[0] and pointer[0] <= 14) and
            (0 <= pointer[1] and pointer[1] <= 14)
        ):
            if pointer[1] + 1*direction > 14:
                break
            next_char = board_array[pointer[0]][pointer[1] + 1*direction].val
            pointer = [pointer[0], pointer[1] + 1*direction]
            final_word_dict = {**final_word_dict, **{tuple(pointer): next_char}} if next_char != "" else final_word_dict
        
        return final_word_dict
    
    elif direction == "u":
        direction = -1
        
        while board_array[pointer[0]][pointer[1]].val != "" and (
            (0 <= pointer[0] and pointer[0] <= 14) and
            (0 <= pointer[1] and pointer[1] <= 14)
        ):
            if pointer[1] + 1*direction < 0:
                break
            next_char = board_array[pointer[0] + 1*direction][pointer[1]].val
            pointer = [pointer[0] + 1*direction, pointer[1]]
            final_word_dict = {**{tuple(pointer): next_char}, **final_word_dict} if next_char != "" else final_word_dict
            
        direction = 1
        pointer = position.copy()
        
        while board_array[pointer[0]][pointer[1]].val != "" and (
            (0 <= pointer[0] and pointer[0] <= 14) and
            (0 <= pointer[1] and pointer[1] <= 14)
        ):
            if pointer[1] + 1*direction > 14:
                break
            next_char = board_array[pointer[0] + 1*direction][pointer[1]].val
            pointer = [pointer[0] + 1*direction, pointer[1]]
            final_word_dict = {**final_word_dict, **{tuple(pointer): next_char}} if next_char != "" else final_word_dict
        
        return final_word_dict
    
    else:
        raise ScrabbleError("Invalid direction for function createWord")        

def checkNewWords(index, word, direction, position, board):
    # based on the index and word and direction determine if to check 3 spaces or only 2
        # if l, index = 0, check behind and top bottom, but if index = 1, then only top and bottom, etc.
    # check the objects around current
    # if direction == "l":
    #     if index == 0:
    #         if (board.get(position[0] + 1, position[1]).isalpha() or 
    #             board.get(position[0] - 1, position[1]).isalpha()):
    #             pass            
    #     elif index == len(word) - 1 or index == -1:
    #         pass
    #     else:
    #         pass
    
    # if 
    
    if board.get(position[0] + 1, position[1]).isalpha():
        word = createWord
        
    # use a recursive algorithm to check words that were made in line with the current word
    pass

def getScore(wordList, board):
    # [{cell object1, obj2,...}, {word2}, {word3}...]
    # REWRITE SO IT USES CELL OBJECTS
    powerups_used = []
    total_points = 0
    

    
    for wordDict in wordList:
        
        word_points = 0
        WordMultipler = 0
        
        for coordinate in wordDict:
            upperletter = wordDict[coordinate].upper()
            coordinate_list = list(coordinate)
            
            if coordinate_list in powerupList and board.board_array[coordinate[0]][coordinate[1]].ID != 0:
                powerups_used.append(coordinate_list)
                if coordinate_list in DoubleLetter:
                    word_points += scrabble_points[upperletter] * 2
                elif coordinate_list in TripleLetter:
                    word_points += scrabble_points[upperletter] * 3
                elif coordinate_list in DoubleWord:
                    WordMultipler = 2
                    word_points += scrabble_points[upperletter]
                elif coordinate_list in TripleWord:
                    if WordMultipler == 3:
                        word_points += scrabble_points[upperletter] * 3
                        continue
                    WordMultipler = 3
                    word_points += scrabble_points[upperletter]
                
            else:
                word_points += scrabble_points[upperletter]
        
        
        if WordMultipler:
            total_points += word_points * WordMultipler
            continue
        
        total_points += word_points
            
    set_powerups = {(x[0],x[1]) for x in powerups_used}
    for powerup_loc in set_powerups:
        board.board_array[powerup_loc[0]][powerup_loc[1]].ID = 0
        # remove powerups from the turn
        
    
    return total_points, powerups_used