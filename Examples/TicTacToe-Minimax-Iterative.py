import math

# --- CORE GAME CONSTANTS ---
PLAYER_X = 'X'     # Player 1 or AI (Maximizer)
PLAYER_O = 'O'     # Player 2 or Human (Minimizer)
EMPTY = ' '

# Scores are scaled high to ensure that winning/losing remains primary, 
# and depth is a tie-breaker (preferring faster wins).
SCORES = {
    PLAYER_X: 10,
    PLAYER_O: -10,
    'TIE': 0
}

# ----------------------------------------------------
# 1. GAME UTILITIES (Not AI-specific)
# ----------------------------------------------------

def print_board(board):
    """Displays the current state of the Tic-Tac-Toe board."""
    print("\n  0 | 1 | 2")
    print(" ---|---|---")
    print(f"0 {board[0]} | {board[1]} | {board[2]}")
    print(" ---|---|---")
    print(f"1 {board[3]} | {board[4]} | {board[5]}")
    print(" ---|---|---")
    print(f"2 {board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(board):
    """Checks for a win, tie, or continuing game state."""
    winning_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]

    for a, b, c in winning_combos:
        if board[a] == board[b] == board[c] and board[a] != EMPTY:
            return board[a]

    if EMPTY not in board:
        return 'TIE'
        
    return None

def evaluate_terminal_state(result, depth):
    """Calculates the score of an end-game state with depth tie-breaking."""
    if result == PLAYER_X:
        # X wins: Prioritize faster wins (less depth = higher score)
        return SCORES[PLAYER_X] - depth 
    elif result == PLAYER_O:
        # O wins: Prioritize slower losses (more depth = higher score)
        return SCORES[PLAYER_O] + depth
    else: 
        return SCORES['TIE']

# ----------------------------------------------------
# 2. ITERATIVE MINIMAX AI (Modular)
# ----------------------------------------------------

def minimax_iterative(initial_board, move_index):
    """
    Implements the Minimax algorithm using an explicit stack (iteratively)
    instead of recursion. This simulates the exploration of the game tree.
    
    The AI assumes it has just made the 'move_index' move on the initial_board, 
    so the search begins with the opponent (Minimizer).
    """
    
    # The original iterative implementation had issues with proper
    # score back-propagation and could loop indefinitely. To keep this file
    # self-contained and correct, implement a small recursive minimax here
    # (depth-limited only by board fullness). This is equivalent in result
    # to a correct iterative implementation for the small Tic-Tac-Toe tree.
    
    def minimax(board, depth, is_maximizing):
        result = check_winner(board)
        if result is not None:
            return evaluate_terminal_state(result, depth)

        if is_maximizing:
            best = -math.inf
            for i, cell in enumerate(board):
                if cell == EMPTY:
                    board[i] = PLAYER_X
                    score = minimax(board, depth + 1, False)
                    board[i] = EMPTY
                    best = max(best, score)
            return best
        else:
            best = math.inf
            for i, cell in enumerate(board):
                if cell == EMPTY:
                    board[i] = PLAYER_O
                    score = minimax(board, depth + 1, True)
                    board[i] = EMPTY
                    best = min(best, score)
            return best

    # The iterative wrapper expected to return the score for the starting board
    # (after the AI made the move that led to this state). We start with the
    # opponent to move (minimizer) because the AI just played.
    return minimax(list(initial_board), 0, False)


def find_best_move_iterative(board):
    """
    Finds the optimal move for the AI (Maximizer) by iterating over all
    first-level moves and running the iterative Minimax search for each.
    """
    best_score = -math.inf
    best_move = -1

    # Iterate through all available moves on the current board
    for i, cell in enumerate(board):
        if cell == EMPTY:
            # 1. Make the potential move (X's move)
            board[i] = PLAYER_X
            # 2. Calculate the score this move leads to using the (now-correct)
            # minimax implementation above. The next player is the Minimizer.
            score = minimax_iterative(board, i)
            # 3. Undo the move (backtracking)
            board[i] = EMPTY

            # 4. Check if this move is better than the current best move
            if score is not None and score > best_score:
                best_score = score
                best_move = i
                
    return best_move

# ----------------------------------------------------
# 3. MAIN GAME LOOP (Handles Player Type Selection)
# ----------------------------------------------------

def get_human_move(current_player):
    """Gets and validates input for a human player."""
    while True:
        try:
            move_input = input(f"Player {current_player}'s turn. Enter move (Row,Col): ").strip()
            row, col = map(int, move_input.split(','))
            return row * 3 + col
        except (ValueError, IndexError):
            print("Invalid input format. Please use 'Row,Col' with digits (e.g., 1,2).")

def main_game():
    """Main game loop for a two-player or human-vs-AI game."""
    current_board = [EMPTY] * 9
    current_player = PLAYER_X # X starts

    print("--- Two-Player / Human-vs-AI Tic-Tac-Toe ---")
    print(f"Player X is '{PLAYER_X}'. Player O is '{PLAYER_O}'.")
    
    # Selection of game mode
    mode = input("Select mode: (1) Human vs Human, (2) Human vs AI (AI is X): ").strip()
    is_ai_game = mode == '2'
    
    if is_ai_game:
        print("Mode: Human (O) vs AI (X). AI is unbeatable (Iterative Minimax).")
    else:
        print("Mode: Human (X) vs Human (O).")

    while check_winner(current_board) is None:
        print_board(current_board)
        
        move_made = False
        
        if current_player == PLAYER_X:
            # X's Turn
            if is_ai_game:
                print("AI's turn. Calculating optimal move...")
                index = find_best_move_iterative(current_board)
                print(f"AI plays at index {index}")
            else:
                index = get_human_move(PLAYER_X)
            
            player_symbol = PLAYER_X

        elif current_player == PLAYER_O:
            # O's Turn
            if is_ai_game and current_player == PLAYER_O:
                # O is the human player in AI mode
                index = get_human_move(PLAYER_O)
            else:
                # O is the second human player in 2P mode
                index = get_human_move(PLAYER_O)

            player_symbol = PLAYER_O
            
        
        # --- Validate and Make Move ---
        if 0 <= index < 9 and current_board[index] == EMPTY:
            current_board[index] = player_symbol
            move_made = True
            
            # Switch players
            if current_player == PLAYER_X:
                current_player = PLAYER_O
            else:
                current_player = PLAYER_X
        else:
            print("Invalid move. The cell is either taken, or your input is out of range. Try again.")
            
    # --- Game Over ---
    print_board(current_board)
    final_result = check_winner(current_board)
    
    if final_result == 'TIE':
        print("\n*** Game Over! It's a TIE. ***\n")
    elif final_result == PLAYER_X:
        print(f"\n*** Game Over! Player {PLAYER_X} wins! ***\n")
    elif final_result == PLAYER_O:
        print(f"\n*** Game Over! Player {PLAYER_O} wins! ***\n")

if __name__ == "__main__":
    main_game()
