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
    
    def is_valid_killer(self, row, col, num):
        if not self.is_valid(row, col, num):
            return False
        cell_value = self.puzzle[row][col]
        if "killer" in cell_value.rules:
            cage_number, cage_sum = map(int, cell_value.rules["killer"].split('-'))
            cage_sum -= num
            
            for i in range(9):
                for j in range(9):
                    cell = self.puzzle[i][j]
                    if "killer" in cell.rules:
                        if cell.rules["killer"].split('-')[0] == str(cage_number):
                            cage_sum -= cell.value
                            if cage_sum < 0:
                                return False
        return True
    
    def solve_killer(self):
        for row in range(9):
            for col in range(9):
                if self.puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid_killer(row, col, num):
                            self.puzzle[row][col] = num
                            if self.solve_killer():
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