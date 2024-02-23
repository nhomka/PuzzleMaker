from pandas import read_csv
from CellValue import CellValue

class Sudoku:
    
    def __init__(self):
        self.puzzle = None
        self.solution = None
        self.rules = {"standard": self.is_valid}
        
    def add_rule(self, rule_name, rule_function):
        self.rules[rule_name] = rule_function
        
    def update_puzzle_to_cell_values(self):
        for row in range(9):
            for col in range(9):
                rules = {}
                cell = self.puzzle[row][col]
                for rule in cell.split(';')[:-1]:
                    rule_name, rule_value = rule.split(':')
                    rules[rule_name] = rule_value.split('-')
                    
                self.puzzle[row][col] = CellValue(cell[-1], self.rules)

    def read_puzzle_from_csv(self, file_path):
        csv_puzzle = read_csv(file_path, header=None)
        self.puzzle = csv_puzzle.iloc[:9, :9].values.tolist()
        
    def read_solution_from_csv(self, file_path):
        csv_solution = read_csv(file_path, header=None)
        self.solution = csv_solution.iloc[:9, :9].values.tolist()
        
    def is_valid(self, row, col, num):
        for x in range(9):
            if self.puzzle[row][x] == num:
                return False
            if self.puzzle[x][col] == num:
                return False
            if self.puzzle[row - row % 3 + x // 3][col - col % 3 + x % 3] == num:
                return False
        return True
    
    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.puzzle[row][col] = num
                            if self.solve():
                                return True
                            self.puzzle[row][col] = 0
                    return False
        return True
    
    def is_solved(self):
        return self.puzzle == self.solution
    
    def print_puzzle(self):
        for row in range(9):
            print(self.puzzle[row])
            
    def print_solution(self):
        for row in range(9):
            print(self.solution[row])
    
    def __str__(self):
        for row in range(9):
            print(self.puzzle[row])