from CellValue import CellValue
from PuzzleReader import PuzzleReader

class Sudoku:
    
    def __init__(self):
        self.raw_puzzle = None
        self.puzzle = None
        self.solution = None
        self.rules = {"standard": self.cell_value_is_valid}
        self.puzzleReader = PuzzleReader(self)
    
    def load_from_file(self, puzzle_file, solution_file = None):
        self.puzzleReader.read_puzzle_from_csv(puzzle_file)
        if solution_file:
            self.puzzleReader.read_solution_from_csv(solution_file)
    
    def add_rule(self, rule_name, rule_function):
        self.rules[rule_name] = rule_function
        
    def update_raw_puzzle_to_cell_values(self):
        for row in range(9):
            for col in range(9):
                cell_contents = str(self.raw_puzzle[row][col])
                self.puzzle[row][col] = CellValue(cell_contents)
        
    def cell_value_is_valid(self, row, col, num):
        for x in range(9):
            if self.puzzle[row][x].value == num:
                return False
            if self.puzzle[x][col].value == num:
                return False
            if self.puzzle[row - row % 3 + x // 3][col - col % 3 + x % 3].value == num:
                return False
        return True
    
    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col].value == 0:
                    for num in range(1, 10):
                        if self.cell_value_is_valid(row, col, num):
                            self.puzzle[row][col].value = num
                            if self.solve():
                                return True
                            self.puzzle[row][col].value = 0
                    return False
        return True
    
    def get_puzzle_values(self):
        return [[self.puzzle[row][col].value for col in range(9)] for row in range(9)]
    
    def is_solved(self):
        return self.get_puzzle_values() == self.solution
    
    def print_raw_puzzle(self):
        for row in range(9):
            print(self.raw_puzzle[row])
            
    def print_puzzle(self):
        for row in range(9):
            print([self.puzzle[row][col].value for col in range(9)])
            
    def print_solution(self):
        for row in range(9):
            print(self.solution[row])
    
    def __str__(self):
        for row in range(9):
            print(self.puzzle[row])