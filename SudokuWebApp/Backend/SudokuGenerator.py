from random import choice

def makePuzzle():
    create_random_solved_puzzle()
    return 

def create_random_solved_puzzle():
    choices = makeChoices()
    puzzle = makeEmptyPuzzle()
    
def makeChoices():
    return [i for i in range(1, 10) for _ in range(9)]
    
def makeEmptyPuzzle():
    return [[0 for _ in range(9)] for _ in range(9)]

def randomValidValue(availableValues):
    return choice(availableValues)


