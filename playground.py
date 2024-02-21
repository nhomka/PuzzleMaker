from Sudoku import Sudoku

puzzle = Sudoku()
puzzle.read_puzzle_from_csv('sudoku_puzzle.csv')
puzzle.read_solution_from_csv('sudoku_solution.csv')

print(f"puzzle: {puzzle.puzzle}")
print(f"solution: {puzzle.solution}")

puzzle.solve()
print(f"solved: {puzzle.puzzle}")
