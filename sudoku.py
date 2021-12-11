
#finding empty spaces in our sudoku puzzle
def find_empty_space(puzzle):              
    for r in range(9):
        for c in range(9):
            if (puzzle[r][c]==0):
                return r,c
    return None,None 
# To know our guess is valid or not
def is_Valid(puzzle, guess, row, col):
    row_val=puzzle[row]
    if guess in row_val:# To check validity in row 
        return False
    col_val=[puzzle[i][col] for i in range(9)]# To check validity in column 
    if guess in col_val:
        return False
    
    # To find the validity in the 3X3 square box
    row_start=(row//3)*3
    col_start=(col//3)*3
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c]== guess:
                return False
    return True
    

def solve_sudoku(puzzle):
    row,col=find_empty_space(puzzle)
    if row is None:
        return True
    for guess in range(1,10):
        if is_Valid(puzzle, guess, row, col):
            puzzle[row][col]= guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col]=0
    return False

if __name__=="__main__":
    example=[
        [3,9,0, 0,5,0, 0,0,0],
        [0,0,0, 2,0,0, 0,0,5],
        [0,0,0, 7,1,9, 0,8,0],
        
        [0,5,0, 0,6,8, 0,0,0],
        [2,0,6, 0,0,3, 0,0,0],
        [0,0,0, 0,0,0, 0,0,4],
        
        [5,0,0, 0,0,0, 0,0,0],
        [6,7,0, 0,0,5, 0,4,0],
        [0,0,9, 0,0,0, 2,0,0]
        ]
    print(solve_sudoku(example))
    print(example)
