import numpy as np

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    if all(board[row][col] != ' ' for row in range(3) for col in range(3)):
        return 'Tie'

    return None

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -1
    if winner == 'O':
        return 1
    if winner == 'Tie':
        return 0

    if is_maximizing:
        best_score = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -np.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True
    
        try:
            row, col = map(int, input("Enter your move (row and column: 0 1 2): ").split())
            if board[row][col] != ' ':
                print("Invalid move. Try again.")
                continue
            board[row][col] = 'X'
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers between 0 and 2.")
            continue

        print_board(board)
        if check_winner(board):
            print("Game Over! Winner:", check_winner(board))
            break

        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
        print("AI's move:")
        print_board(board)

        if check_winner(board):
            print("Game Over! Winner:", check_winner(board))
            break

play_tic_tac_toe()
