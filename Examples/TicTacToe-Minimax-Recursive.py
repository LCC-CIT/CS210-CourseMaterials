import math

# Constants for the game
AI_PLAYER = 'X'     # The Maximizer
HUMAN_PLAYER = 'O'  # The Minimizer
EMPTY = ' '

# FIX APPLIED HERE: Scores are increased to ensure depth adjustment does not flip the sign.
# Max depth is 9. Using +/- 10 keeps wins positive and losses negative.
SCORES = {
    AI_PLAYER: 10,
    HUMAN_PLAYER: -10,
    'TIE': 0
}

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
    """Checks if any player has won, or if the game is a draw."""
    winning_combos = [
        # Rows
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Columns
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Diagonals
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combos:
        if board[a] == board[b] == board[c] and board[a] != EMPTY:
            return board[a] # Returns 'X' or 'O' (the winner)

    # Check for tie (no winner AND no empty cells)
    if EMPTY not in board:
        return 'TIE'
        
    return None # Game is not over yet

def minimax(board, depth, is_maximizing):
    """
    The core Minimax algorithm. It recursively searches the game tree
    to find the optimal score for the current player.

    :param board: The current state of the game board.
    :param depth: How many moves deep the algorithm has searched (used for tie-breaking).
    :param is_maximizing: True if it's the AI's turn (Maximizer), False if it's the Human's (Minimizer).
    :return: The score of the best outcome achievable from this state.
    """
    
    # 1. BASE CASE: Check if the game is over (terminal node)
    result = check_winner(board)
    if result is not None:
        # Scoring logic is corrected:
        if result == AI_PLAYER:
            # Prioritize faster wins (less depth = higher score)
            # Example: 10 - 2 = 8 (better than 10 - 8 = 2)
            return SCORES[AI_PLAYER] - depth 
        elif result == HUMAN_PLAYER:
            # Prioritize slower losses (more depth = higher score)
            # Example: -10 + 8 = -2 (better than -10 + 2 = -8)
            return SCORES[HUMAN_PLAYER] + depth
        else: # 'TIE'
            return SCORES['TIE'] # Score is 0
            
    # 2. RECURSIVE STEP: Maximizing Player (AI - 'X')
    if is_maximizing:
        best_score = -math.inf # Start with the worst possible score
        
        for i, cell in enumerate(board):
            if cell == EMPTY:
                # 1. Make the move (hypothetically)
                board[i] = AI_PLAYER
                # 2. Recurse for the Minimizing player (next turn)
                score = minimax(board, depth + 1, False)
                # 3. Undo the move (backtracking)
                board[i] = EMPTY 
                # 4. Choose the maximum score returned by the branches
                best_score = max(best_score, score)
        return best_score

    # 3. RECURSIVE STEP: Minimizing Player (Human - 'O')
    else: 
        best_score = math.inf # Start with the worst possible score for the maximizer
        
        for i, cell in enumerate(board):
            if cell == EMPTY:
                # 1. Make the move (hypothetically)
                board[i] = HUMAN_PLAYER
                # 2. Recurse for the Maximizing player (next turn)
                score = minimax(board, depth + 1, True)
                # 3. Undo the move (backtracking)
                board[i] = EMPTY 
                # 4. Choose the minimum score returned by the branches
                best_score = min(best_score, score)
        return best_score

def find_best_move(board):
    """
    Finds the optimal move for the AI (Maximizing Player) by calling Minimax 
    on all possible starting moves.
    """
    best_score = -math.inf
    best_move = -1

    # Iterate through all available moves on the current board
    for i, cell in enumerate(board):
        if cell == EMPTY:
            # 1. Make the potential move
            board[i] = AI_PLAYER
            # 2. Calculate the score this move leads to (assuming optimal play from both sides)
            # We call minimax starting with the Minimizing player (False) because we just made the move.
            score = minimax(board, 0, False)
            # 3. Undo the move (backtracking)
            board[i] = EMPTY

            # 4. Check if this move is better than the current best move
            if score > best_score:
                best_score = score
                best_move = i
                
    return best_move

def main_game():
    """Main game loop for Tic-Tac-Toe."""
    # The board is a list of 9 elements representing the 3x3 grid
    current_board = [EMPTY] * 9
    current_player = HUMAN_PLAYER # Human goes first

    print("--- Tic-Tac-Toe Minimax AI ---")
    print("LOGIC FIX APPLIED: AI should now be unbeatable.")
    print(f"You are '{HUMAN_PLAYER}' (Minimizer). The AI is '{AI_PLAYER}' (Maximizer).")
    print("Enter your move as 'Row,Col' (e.g., '1,2' for the center-right square).")

    while check_winner(current_board) is None:
        print_board(current_board)

        if current_player == HUMAN_PLAYER:
            # --- Human Player's Turn ---
            try:
                move_input = input(f"Your turn ({HUMAN_PLAYER}). Enter move (Row,Col): ").strip()
                row, col = map(int, move_input.split(','))
                index = row * 3 + col
                
                if 0 <= index < 9 and current_board[index] == EMPTY:
                    current_board[index] = HUMAN_PLAYER
                    current_player = AI_PLAYER
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input format. Please use 'Row,Col'.")
                
        else:
            # --- AI Player's Turn (Minimax in action!) ---
            print(f"AI's turn ({AI_PLAYER}). Calculating optimal move...")
            
            # The AI uses the Minimax algorithm to find its move
            ai_move_index = find_best_move(current_board)
            
            if ai_move_index != -1:
                current_board[ai_move_index] = AI_PLAYER
                current_player = HUMAN_PLAYER
            else:
                break

    # --- Game Over ---
    print_board(current_board)
    final_result = check_winner(current_board)
    
    if final_result == AI_PLAYER:
        print("\nGame Over! The AI (X) wins. This is the optimal outcome for the Maximizer.\n")
    elif final_result == HUMAN_PLAYER:
        print("\nGame Over! You (O) won! If the AI loses, it means the logic is still flawed!\n")
    else:
        print("\nGame Over! It's a TIE. A truly optimal game by both sides always ends in a draw for Tic-Tac-Toe.\n")

if __name__ == "__main__":
    main_game()
