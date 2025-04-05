'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.


'''
from collections import defaultdict

def isValidSudoku(board: list[list[str]]) -> bool:

    '''
        rows = {0: {5,3,7},
                1: (6,1,9,5),
                ...}
        
        columns = {0: {5,6,8,4,7},
                   1: {3,9,6},
                   ...}
        
        // board is devided by 3x3 
        // 0 // 3 = 0
        // 1 // 3 = 0
        // 2 // 3 = 0
        // 3 // 3 = 1
        // 4 // 3 = 1
        squares = {(0,0): {5,3,6,9,8},  
                   (0,1): {7,1,9,5},
                   (0,2): {6},
                   (1,0): {8,4,7},
                   ...}
    '''

    # dict of set where 
    # key = row number
    # value = set of numbers in that row
    rows = defaultdict(set)

    # dict of set where 
    # key = column number
    # value = set of numbers in that column
    columns = defaultdict(set)

    # dict of set where 
    # key = a tuple indication which square (0,0) or (0,1) ---> See above for more
    # value = set of numbers in that square
    squares = defaultdict(set)

    for row in range(9):
        for column in range(9):

            # ignore "."
            if board[row][column] == ".":
                continue

            if board[row][column] in rows[row]:
                return False
            
            if board[row][column] in columns[column]:
                return False
            
            if board[row][column] in squares[(row // 3, column // 3)]:
                return False

            rows[row].add(board[row][column])
            columns[column].add(board[row][column])
            squares[(row // 3, column // 3)].add(board[row][column])

    return True


if __name__ == "__main__":

    board1 = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]
]

    board2 = [
["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

    print(isValidSudoku(board1)) # True
    print(isValidSudoku(board2)) # False
