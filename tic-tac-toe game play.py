
def display_board(board):
  """Prints the current game board."""
  for row in board:
    for cell in row:
      print(cell, end=" ")
    print()

def is_valid_move(board, row, col):
  """Checks if a move is valid (cell is empty)."""
  return board[row][col] == " "

def make_move(board, player, row, col):
  """Places the player's mark on the board."""
  board[row][col] = player

def is_winner(board, player):
  """Checks if a player has won."""
  # Check rows
  for row in board:
    if all(cell == player for cell in row):
      return True
  # Check columns
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True
  # Check diagonals
  if all(board[row][row] == player for row in range(3)):
    return True
  if all(board[row][2 - row] == player for row in range(3)):
    return True
  return False

def is_board_full(board):
  """Checks if all cells are filled."""
  return all(cell != " " for row in board for cell in row)

def main():
  """Runs the tic-tac-toe game."""
  board = [[" " for _ in range(3)] for _ in range(3)]
  current_player = "X"

  while True:
    display_board(board)

    # Get player move
    while True:
      row, col = map(int, input(f"Player {current_player}, enter your move (row col): ").split())
      if 0 <= row <= 2 and 0 <= col <= 2 and is_valid_move(board, row, col):
        break
      else:
        print("Invalid move. Try again.")

    make_move(board, current_player, row, col)

    # Check for winner or tie
    if is_winner(board, current_player):
      display_board(board)
      print(f"Player {current_player} wins!")
      break
    elif is_board_full(board):
      display_board(board)
      print("It's a tie!")
      break

    # Switch player
    current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
  main()