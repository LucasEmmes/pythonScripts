import sudoku_functions
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
        
# Added *args purely so that it can be started off
# with solve() instead of solve(0). Looks nicer imo
def solve(*args):
    # Keeps track of where we are
    if len(args) == 0:
        n = 0
    else:
        n = args[0]

    # Checks if we have passed 81 tiles (i.e. we are done)
    if n == 81:
        sudoku_functions.print_sudoku(sudoku)
        return sudoku
    
    x = n%9
    y = n//9

    # Skips this tile if it was filled in by the base
    if sudoku_base[y][x] != 0:
        grid = solve(n+1)
        if grid:
            return grid
    # Otherwise iterate through all allowed values
    # and pass along after each iteration to test it
    else:
        taken = sudoku_functions.get_taken(x,y,sudoku)
        for i in range(1,10):
            if i not in taken:
                sudoku[y][x] = i
                grid = solve(n+1)
                if grid:
                    return grid

    # If we reach this point, it means we messed up earlier
    # Remove current guesses and try with different previous values
    sudoku[y][x] = 0

    # If we fail at tile 0, the sudoku is unsolvable
    if n == 0:
        print("Could not solve")
    return False

solved_sudoku = solve()
cmd_pause = input()

# Coded by Lucas Emmes on 26/02/21 - 27/02/21 when he could have
# been doing homework instead :^)
