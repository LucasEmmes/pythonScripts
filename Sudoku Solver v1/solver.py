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

def check_row(n):
    result = []
    for v in sudoku[n]:
        if v != 0:
            result.append(v)
    return result

def check_col(n):
    result = []
    for v in [sudoku[i][n] for i in range(9)]:
        if v != 0:
            result.append(v)
    return result

def check_block(x,y):
    n = (y//3)*3+(x//3)
    block_col = n%3
    block_row = n//3
    
    result = []
    for row in [sudoku[y] for y in range(block_row*3, block_row*3+3)]:
        for v in [row[x] for x in range(block_col*3, block_col*3+3)]:
            if v != 0:
                result.append(v)
    return result
            
def check_win():
    for row in sudoku:
        for v in row:
            if v == 0:
                return False
    return True


def print_sudoku(s):
    result = ""
    for i in range(3):
        for j in range(3):
            row = sudoku[3*i+j]
            for k in range(3):
                result += f"{row[k+0]} {row[k+1]} {row[k+2]}"
                if k != 2:
                    result += " | "
            result += "\n"
        if i != 2:
            result += "- - - - - - - - - - -\n"
    print(result)
        
# Added *args purely so that it can be started off
# with solve() instead of solve(0). Looks nicer imo
def solve(*args):
    if len(args) == 0:
        n = 0
    else:
        n = args[0]
    
    if n == 81:
        print_sudoku(sudoku)
        return sudoku
    
    x = n%9
    y = n//9
    
    if sudoku_base[y][x] != 0:
        grid = solve(n+1)
        if grid:
            return grid
    else:
        taken = set(check_col(x) + check_row(y) + check_block(x,y))
        for i in range(1,10):
            if i not in taken:
                sudoku[y][x] = i
                grid = solve(n+1)
                if grid:
                    return grid
                
    sudoku[y][x] = 0

    if n == 0:
        print("Could not solve")
    return False

solved_sudoku = solve()
cmd_pauser = input()

# Coded by Lucas Emmes on 26/02/21 - 27/02/21 when he could have
# been doing homework instead :^)
