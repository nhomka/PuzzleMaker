from pandas import read_csv

class Sudoku:
    
    def __init__(self):
        self.puzzle = None
        self.solution = None

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