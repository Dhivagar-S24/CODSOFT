import math

board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("--+---+--")
    print("\n")


def is_winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    return any(all(brd[pos] == player for pos in combo) for combo in win_conditions)

def is_draw():
    return " " not in board

def make_move(position, player):
    if board[position] == " ":
        board[position] = player
        return True
    return False

def get_best_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def minimax(brd, depth, is_maximizing):
    if is_winner(brd, "O"):
        return 1
    elif is_winner(brd, "X"):
        return -1
    elif " " not in brd:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, depth + 1, False)
                brd[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, depth + 1, True)
                brd[i] = " "
                best_score = min(score, best_score)
        return best_score

def play_game():
    print(" Welcome to Tic-Tac-Toe AI!")
    print("You are 'X' and the AI is 'O'. Choose positions (0 to 8).")
    print_board()
    current_player = "X"

    while True:
        if current_player == "X":
            try:
                position = int(input("Your move (0-8): "))
                if position not in range(9):
                    print(" Invalid position. Choose 0–8.")
                    continue
            except ValueError:
                print(" Please enter a valid number.")
                continue
        else:
            position = get_best_move()
            print(f" AI chose position {position}")

        if make_move(position, current_player):
            print_board()

            if is_winner(board, current_player):
                print(f" {current_player} wins!")
                break
            elif is_draw():
                print(" It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"
        else:
            print(" Spot already taken. Try again.")

# Start the game
play_game()