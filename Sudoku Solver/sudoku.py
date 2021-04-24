def check_row(n, sudoku):
    result = []
    for v in sudoku[n]:
        if v != 0:
            result.append(v)
    return result

def check_col(n, sudoku):
    result = []
    for v in [sudoku[i][n] for i in range(9)]:
        if v != 0:
            result.append(v)
    return result

def check_block(x,y, sudoku):
    n = (y//3)*3+(x//3)
    block_col = n%3
    block_row = n//3
    
    result = []
    for row in [sudoku[y] for y in range(block_row*3, block_row*3+3)]:
        for v in [row[x] for x in range(block_col*3, block_col*3+3)]:
            if v != 0:
                result.append(v)
    return result

def print_sudoku(s):
    result = ""
    for i in range(3):
        for j in range(3):
            row = s[3*i+j]
            for k in range(3):
                result += f"{row[k+0]} {row[k+1]} {row[k+2]}"
                if k != 2:
                    result += " | "
            result += "\n"
        if i != 2:
            result += "- - - - - - - - - - -\n"
    print(result)

def get_taken(x,y,sudoku):
    return set(check_col(x, sudoku) + check_row(y, sudoku) + check_block(x,y, sudoku))

def solve(sudoku, sudoku_base, *args):
    """
    Solves any standard (and solvable) sudoku through recursion
    PARAMS:
        sudoku (arr[row][col]): array of the sudoku in the form arr[[row1], [row2], ...]. Use 0 as a placeholder for empty tiles. This array wil be updated in-place
        sudoku_base (arr[row][col]): copy of the sudoku, used to keep track of which tiles to fill in (this does not change)
        *args (int): which iteration / tile we are on. Really only used for recursion purposes. Can and should be ignored
    RETURNS:
        If sudoku can be solved: arr[row][col]: solved sudoku array
        If the sudoku cannot be solved: False
    """


    # Keeps track of where we are
    if len(args) == 0:
        n = 0
    else:
        n = args[0]

    # Checks if we have passed 81 tiles (i.e. we are done)
    if n == 81:
        return sudoku
    
    x = n%9
    y = n//9

    # Skips this tile if it was filled in by the base
    if sudoku_base[y][x] != 0:
        grid = solve(sudoku, sudoku_base, n+1)
        if grid:
            return grid
    # Otherwise iterate through all allowed values
    # and pass along after each iteration to test it
    else:
        taken = get_taken(x,y,sudoku)
        for i in range(1,10):
            if i not in taken:
                sudoku[y][x] = i
                grid = solve(sudoku, sudoku_base, n+1)
                if grid:
                    return grid

    # If we reach this point, it means we messed up earlier
    # Remove current guesses and try with different previous values
    sudoku[y][x] = 0

    # If we fail at tile 0, the sudoku is unsolvable
    if n == 0:
        print("Could not solve")
    return False

# Coded by Lucas Emmes on 26/02/21 - 27/02/21 when he could have
# been doing homework instead :^)