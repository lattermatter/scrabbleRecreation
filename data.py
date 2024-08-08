def rotateCC(list):
    # translate the point, rotate it, then translate it back
    return [[point[1], 2*7 - point[0]] for point in list]

def create_all_section(list):
    return list + rotateCC(list) + rotateCC(rotateCC(list)) + rotateCC(rotateCC(rotateCC(list)))

DL, TL, DW, TW = 102, 103, 200, 300

DoubleLetter = create_all_section([[0,3], [3,0], [2,6], [6,2], [6,6], [3,7]])
TripleLetter = create_all_section([[1,5], [5,1], [5,5]])
DoubleWord = create_all_section([[1,1], [2,2], [3,3], [4,4]]) + [[7,7]]
TripleWord = create_all_section([[0,0], [0,7]])

powerupList = DoubleLetter + TripleLetter + DoubleWord + TripleWord

powerupDict = {DL: DoubleLetter,
           TL: TripleLetter,
           DW: DoubleWord,
           TW: TripleWord}

opener = DoubleWord[-1]
boardLength = 15

scrabble_points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}


def setCheck(set, iterable):
    for element in iterable:
        if element not in set:
            return False
    return True

