rules = {
    "KillerCages" : "Dotted lines form cages around groups of cells. \
    The number in the top-left corner is the sum of all values in the cage.",
    "Thermometers" : "The numbers must increase as you move along the thermometer.",
    "SymmetryLines" : "The numbers on the line must be symmetrical starting from both ends.",
    "NoAdjacent" : "No number can appear directly adjacent or diagonally to another number of the same value.",
    "UniqueDiagonals" : "Each number must appear once in each diagonal.",
    "DiagonalSums" : "A number and arrow outside the grid indicate the sum of the numbers in the diagonal.",
    "BlackDots" : "A black dot connects two cells.  One value must be twice the value of the other.",
    "WhiteDots" : "A white dot connects two cells.  The numbers in those cells must be consecutive.",
    "QuarteredCircles" : "A circle connects four cells. Any number in the circle must be found in one of the four cells.",
    "XsAndVs" : "Any two cells connected by an X must sum to 10.  Any two cells connected by a V must sum to 5.",
}

class Rules:
    name = ""
    full_description = ""
    format = ""
    example_puzzle = None