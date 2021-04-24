import sudoku as sudoku_solver

# Sudoku yoinked from https://sudoku.com/expert/
sudoku_base = [
[0,7,8,5,0,0,0,0,0],
[0,0,3,0,0,7,8,0,0],
[0,0,0,1,9,0,0,0,0],
[0,0,7,0,0,0,2,9,0],
[0,9,0,0,6,1,0,4,0],
[0,0,0,0,0,4,0,0,0],
[3,0,6,0,0,2,0,0,0],
[0,1,0,0,0,0,0,0,4],
[0,0,0,0,0,0,5,0,0]
]

# I use the base to find out which values to skip
# "Sudoku" is the array that gets modified throughout the process
sudoku = sudoku_base.copy()

solved_sudoku = sudoku_solver.solve(sudoku, sudoku_base)
sudoku_solver.print_sudoku(solved_sudoku)
pause = input()