from data import *

class Cell():
    def __init__(self, row, col, connections={}, val=""):
        self.row = row
        self.col = col
        self.val = val
        self.connections = connections
        self.ID = 0
        for ID, powerup in powerupDict.items():
            if [self.row, self.col] in powerup:
                self.ID = ID
                break
            
    def changeID(self):
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
        # add more logic
        super().__init__(*args, **kwargs)

def displayColNumbers():
    string = "  "
    list1 = [f'   {col_num}' for col_num in range(10)]
    string2 = " "
    list2 = [f'  {col_num}' for col_num in range(10, 15)]
    return string + "".join(list1) + string2 + "".join(list2) + "\n"
    
def displayRowNumbers(row):
    return f"{row}  |" if row < 10 else f"{row} |"

# unfinished
def addWord(board, word, direction, position):
    # use CheckNewWords
    # is there a letter in the new position already?
    # if not then add the letter
        # if there is the letter but it is the same one then just raise the function without adding anything
        # if it is diff then raise scrabble error
        # add 1 1,3 3 or 0 0,2 2 based on orientation and position
        # if obj value isalpha
        # check the objects set
        # if len is 4 then dont check for words
        # if it is not then check surrounding words
    try:
        if direction == "l":
            for index in range(len(word)):
                board[position[0]][position[1] + index].val = word[index]
        elif direction == "u":
            for index in range(len(word)):
                board[position[0] + index][position[1]].val = word[index]
        else:
            raise ScrabbleError("Direction incorrect")
        # return [{(x, y): letter,...}, {word2}, {word3}...]
        return board
    except IndexError:
        raise ScrabbleError("word entered reaches out of bounds")
    
    
    

def checkNewWords(index, word, direction):
    # based on the index and word and direction determine if to check 3 spaces or only 2
        # if l, index = 0, check behind and top bottom, but if index = 1, then only top and bottom, etc.
    # check the objects around current
    if direction == "l":
        if index == 0:
            # check back, top, bottom
            filter(lambda cellObj: cellObj.val.isalpha(), )
        elif index == len(word) - 1 or index == -1:
            pass
        else:
            pass
        
    # use a recursive algorithm to check words that were made in line with the current word
    pass

def getScore(wordList):
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
            
            if coordinate_list in powerupList:
                powerups_used.append(coordinate_list)
                if coordinate_list in DoubleLetter:
                    word_points += scrabble_points[upperletter] * 2
                elif coordinate_list in TripleLetter:
                    word_points += scrabble_points[upperletter] * 3
                elif coordinate_list in DoubleWord:
                    WordMultipler = 2
                    word_points += scrabble_points[upperletter]
                elif coordinate_list in TripleWord:
                    WordMultipler = 3
                    word_points += scrabble_points[upperletter]
                
            else:
                word_points += scrabble_points[upperletter]
        
        
        if WordMultipler:
            total_points += word_points * WordMultipler
            print(total_points)
            continue
        
        total_points += word_points
        
        print(total_points)
    
    return total_points, powerups_used