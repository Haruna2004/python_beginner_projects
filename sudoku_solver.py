#sudoku
def find_next_empty(puzzle):
    #find the next row, col in this puzzle that is not filled yet --> rep with -1
    #return row , col tuple (or None, None) if there is none

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c 
    return None, None #if no spaces are in the puzzle
def is_valid(puzzle,guess,row,col):
    #figures out whether the guess at row/col of the puzzle is valid
    #return true if it is valid, False otherwise

    #let's start with the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #now the column
    col_val = [puzzle[i][col] for i in range(9)]
    if guess in col_val:
        return False

    #and then the square
    #we want to get where the 3 x 3 square starts
    #and iterate over the 3 values in the row / col
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    #we we get here this checks pass
    return True


def solve_sudoku(puzzle):
    #solve sudoku using backtracking
    #our puzzle is a list or list with each inner list is a row in our sudoku
    #return whether a solution exist
    #mutate the puzzle to be the solution (if the solution exist)

    #step 1 choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    #step 1.1 if there's nowhere left, then we are done because we only allowed valid inputs 
    if row is None:
        return True
    #step 3: if there is a place to put a number , then make a guess between 1 and 9
    for guess in range(1,10):
        #step 3: check if this is a valid guess
        if is_valid(puzzle,guess,row,col):
            #step 3.1: if this is valid, then place that guess on the puzzle!
            puzzle[row][col] = guess
            #now recurse using this puzzle!
            #recursively call our function
            if solve_sudoku(puzzle):
                return True
        
        #step 5 : if not valid OR if our guess does not solve the puzzle, then we 
        #need to backtrack and try a new number
        puzzle[row][col] = -1
    #step 6: if none of the number we tried work, then this puzzle is UNSOLVABLE!!
    return False


if __name__ == '__main__':
    example_board = [
        [3,9,-1,   -1,5,-1,   -1,-1,-1],
        [-1,-1,-1,   2,-1,-1,   -1,-1,5],
        [-1,-1,-1,   7,1,9,    -1,8,-1],
        
        [-1,5,-1,   -1,6,8,   -1,-1,-1],
        [2,-1,6,     -1,-1,3,   -1,-1-1],
        [-1,-1,-1, -1,-1,-1,   -1,-1,4],

        [5,-1,-1,   -1,-1,-1,   -1,-1,-1],
        [6,7,-1,   -1,-1,5,    -1,4,-1],
        [1,-1,9,    -1,-1,-1,  2,-1,-1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)



