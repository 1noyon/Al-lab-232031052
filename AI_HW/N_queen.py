

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

def is_safe(board, row, col, n):
    
    for i in range(row):
        if board[i][col] == 1:
            return False

    
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueen(board, row, n):
    if row == n:
        print_board(board)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueen(board, row + 1, n):
                return True
            board[row][col] = 0  
    return False


n = int(input("Enter number of Queens (N): "))
board = [[0] * n for _ in range(n)]

if not solve_nqueen(board, 0, n):
    print("No solution exists.")
