# Set initial state
board = [["   " for i in range(3)] for _ in range(3)]

def main():    
    # Initialize players
    while True:
        player = input("Please choose one of the following options: X or O\n").upper()
        if player in ["X", "O"]:
            break
        else:
            print("Invalid input.")

    # CPU gets the opposite symbol
    cpu = "O" if player == "X" else "X"

    # Print initial board state
    print_board()

    # Induce loop
    while True:
        # Check whose turn it is
        if whose_turn() == player:
            # Get player action and validate
            while True:
                action = input("Select a square from 1 to 9: ")
                # Validate action
                if valid_action(action):
                    break
                else:
                    print("Invalid action.")
            # Update board with the action
            update_board(action, player)
            # Check for win or draw:
            if win_or_draw():
                break
        elif whose_turn() == cpu:
            action = choose_action()

            # Let the player know what the CPU chose
            print(f"CPU selects square {action}")
            # Update board with the action
            update_board(action, cpu)
            # Check for win or draw:
            if win_or_draw():
                break


def choose_action() -> str:
    ... # TODO


def congratulate_winner(winner: str) -> None:
    ... # TODO


# Print current state of global board
def print_board():
    print("Current state:\n")

    for index, row in enumerate(board):
        print("|".join(row))
        if index < 2:
            print("-" * 11)


# Figure out whose turn it is, assuming X always goes first
def whose_turn() -> str:
    X_count = O_count = 0
    for row in board:
        for square in row:
            if square == "X":
                X_count += 1
            elif square == "O":
                O_count += 1

    # compare counts to determine turn
    if X_count == 0:
        return "X"
    elif X_count == O_count:
        return "X"
    elif X_count - 1 == O_count:
        return "O"
    else:
        print("Invalid board state. Diagnose and Debug.")
        return "ERROR"
    


def valid_action(action: str) -> bool:
    # Check if action is a number between 1 and 9
    if int(action) not in [i for i in range(1, 10)]:
        return False
    
    # Check if the square is already taken
    row = (int(action) - 1 // 3)
    column = (int(action) - 1 % 3)

    # if the square is not empty, aka "   ", return False
    if board[row][column] != "   ":
        print("Square already taken.")
        return False
    
    return True


def update_board(action: str, user_symbol: str) -> None:
    # Get the coordinates of the action
    row = (int(action) - 1 // 3)
    column = (int(action) - 1 % 3)

    # Update the board with the action
    global board
    board[row][column] = f" {user_symbol} "
    
    print_board()


def win_or_draw():
    # Check rows for win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "   ":
            winner = row[0].strip()
            congratulate_winner(winner)
            return True

    # Check columns for win
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] and board[0][column] != "   ":
            winner = board[0][col].strip()
            congratulate_winner(winner)
            return True


    # Check diagonals for win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "   ":
        winner = board[0][0].strip()
        congratulate_winner(winner)
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "   ":
        winner = board[0][2].strip()
        congratulate_winner(winner)
        return True

    # Check for draw
    for row in board:
        for square in row:
            if square == "   ":
                return False
    return True


if __name__ == "__main__":
    main()