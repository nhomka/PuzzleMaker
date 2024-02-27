from Sudoku import Sudoku
from KillerSudoku import KillerSudoku

puzzle = Sudoku()
puzzle.read_puzzle_from_csv('sudoku_puzzle.csv')
puzzle.read_solution_from_csv('sudoku_solution.csv')

print(f"puzzle:")
puzzle.print_puzzle()
print(f"solution:")
puzzle.print_solution()

puzzle.solve()

print(f"solved:")
puzzle.print_puzzle()
print(f"is_solved: {puzzle.is_solved()}")

puzzle = KillerSudoku()
puzzle.read_puzzle_from_csv('killer_sudoku_puzzle.csv')
puzzle.read_solution_from_csv('killer_sudoku_solution.csv')

print(f"puzzle:")
puzzle.print_puzzle()
print(f"solution:")
puzzle.print_solution()

puzzle.solve()

print(f"solved:")
puzzle.print_puzzle()
print(f"is_solved: {puzzle.is_solved()}")