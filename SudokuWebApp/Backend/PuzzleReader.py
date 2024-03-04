from pandas import read_csv
from Sudoku import Sudoku
from CellValue import CellValue

class PuzzleReader():
    def __init__(self, sudoku):
        self.Sudoku = sudoku
        
    def read_puzzle_from_csv(self, file_path):
        csv_puzzle = read_csv(file_path, header=None)
        self.Sudoku.raw_puzzle = csv_puzzle.iloc[:9, :9].values.tolist()
        self.Sudoku.puzzle = csv_puzzle.iloc[:9, :9].values.tolist()
        self.update_raw_puzzle_to_cell_values()
        
    def read_solution_from_csv(self, file_path):
        csv_solution = read_csv(file_path, header=None)
        self.Sudoku.solution = csv_solution.iloc[:9, :9].values.tolist()
        
    def update_raw_puzzle_to_cell_values(self):
        for row in range(9):
            for col in range(9):
                cell_contents = str(self.raw_puzzle[row][col])
                self.Sudoku.puzzle[row][col] = CellValue(cell_contents)