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
