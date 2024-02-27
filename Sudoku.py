from pandas import read_csv
from CellValue import CellValue

class Sudoku:
    
    def __init__(self):
        self.raw_puzzle = None
        self.puzzle = None
        self.solution = None
        self.rules = {"standard": self.is_valid_cell}
        
    def add_rule(self, rule_name, rule_function):
        self.rules[rule_name] = rule_function
        
    def update_raw_puzzle_to_cell_values(self):
        for row in range(9):
            for col in range(9):
                cell_contents = str(self.raw_puzzle[row][col])
                self.puzzle[row][col] = CellValue(cell_contents)

    def read_puzzle_from_csv(self, file_path):
        csv_puzzle = read_csv(file_path, header=None)
        self.raw_puzzle = csv_puzzle.iloc[:9, :9].values.tolist()
        self.puzzle = csv_puzzle.iloc[:9, :9].values.tolist()
        # self.print_raw_puzzle()
        # self.print_puzzle()
        self.update_raw_puzzle_to_cell_values()
        
    def read_solution_from_csv(self, file_path):
        csv_solution = read_csv(file_path, header=None)
        self.solution = csv_solution.iloc[:9, :9].values.tolist()
        
    def is_valid_cell(self, row, col, num):
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
                        if self.is_valid_cell(row, col, num):
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