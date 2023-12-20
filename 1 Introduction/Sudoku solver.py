# Sudoku solver

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row and column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False

    # Check if 'num' is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_loc = find_empty_location(board)

    if not empty_loc:
        return True  # Puzzle solved

    row, col = empty_loc

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True  # If placing 'num' leads to a solution

            board[row][col] = 0  # Backtrack if 'num' doesn't lead to a solution

    return False  # No number can be placed in the current position

# Example Sudoku puzzle (0 represents an empty cell)
sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku Puzzle:")
print_board(sudoku_puzzle)

if solve_sudoku(sudoku_puzzle):
    print("\nSolved Sudoku:")
    print_board(sudoku_puzzle)
else:
    print("\nNo solution exists.")
