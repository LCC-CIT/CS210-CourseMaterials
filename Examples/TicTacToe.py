import math

# Constants for the game
PLAYER_1 = 'X'
PLAYER_2 = 'O'
EMPTY = ' '

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

def main_game():
    """Main game loop for a two-player console Tic-Tac-Toe game."""
    # The board is a list of 9 elements representing the 3x3 grid
    current_board = [EMPTY] * 9
    current_player = PLAYER_1 # Player X starts

    print("--- Two-Player Console Tic-Tac-Toe ---")
    print(f"Player 1 is '{PLAYER_1}'. Player 2 is '{PLAYER_2}'.")
    print("Enter your move as 'Row,Col' (e.g., '1,2' for the center-right square).")

    while check_winner(current_board) is None:
        print_board(current_board)
        
        try:
            # --- Get Move Input ---
            move_input = input(f"Player {current_player}'s turn. Enter move (Row,Col): ").strip()
            row, col = map(int, move_input.split(','))
            
            # Convert 2D coordinates (Row, Col) to 1D list index (0-8)
            index = row * 3 + col
            
            # --- Validate and Make Move ---
            if 0 <= index < 9 and current_board[index] == EMPTY:
                current_board[index] = current_player
                
                # Switch players for the next turn
                if current_player == PLAYER_1:
                    current_player = PLAYER_2
                else:
                    current_player = PLAYER_1
            else:
                print("Invalid move. The cell is either taken, or your input is out of range. Try again.")
        
        except (ValueError, IndexError):
            print("Invalid input format. Please use 'Row,Col' with digits (e.g., 1,2).")

    # --- Game Over ---
    print_board(current_board)
    final_result = check_winner(current_board)
    
    if final_result == PLAYER_1:
        print("\n*** GAME OVER! Player X wins! ***\n")
    elif final_result == PLAYER_2:
        print("\n*** GAME OVER! Player O wins! ***\n")
    else:
        print("\n*** GAME OVER! It's a TIE. ***\n")

if __name__ == "__main__":
    main_game()
