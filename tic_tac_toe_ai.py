import math

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def is_winner(board, player):
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_states

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha, beta, use_pruning=True):
    if is_winner(board, 'O'): return 1
    if is_winner(board, 'X'): return -1
    if is_full(board): return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta, use_pruning)
                    board[i][j] = ' '
                    best = max(best, score)
                    if use_pruning:
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            return best
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta, use_pruning)
                    board[i][j] = ' '
                    best = min(best, score)
                    if use_pruning:
                        beta = min(beta, score)
                        if beta <= alpha:
                            return best
        return best

def best_move(board, use_pruning=True):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False, -math.inf, math.inf, use_pruning)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    use_pruning = input("Use Alpha-Beta Pruning? (y/n): ").strip().lower() == 'y'
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter col (0, 1, 2): "))
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Cell already occupied.")
            except:
                print("Invalid input. Try again.")

        print_board(board)

        if is_winner(board, 'X'):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        i, j = best_move(board, use_pruning)
        board[i][j] = 'O'
        print_board(board)

        if is_winner(board, 'O'):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
