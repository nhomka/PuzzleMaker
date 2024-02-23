from Sudoku import Sudoku

class KillerSudoku(Sudoku):
    
    def is_valid(self, row, col, num):
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