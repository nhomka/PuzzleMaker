from Sudoku import Sudoku

class KillerSudoku(Sudoku):
    
    def is_valid(self, row, col, num):
        if not super().is_valid(row, col, num):
            return False
        
        cell_value = self.puzzle[row][col]
        
        cage_number, cage_sum = map(int, cell_value.rules["K"])
        cage_sum -= num
        
        for i in range(9):
            for j in range(9):
                cell = self.puzzle[i][j]
                if "K" in cell.rules:
                    if cell.rules["K"][0] == str(cage_number):
                        cage_sum -= cell.value
                        if cage_sum < 0:
                            return False
        return True