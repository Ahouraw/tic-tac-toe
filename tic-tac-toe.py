def main():
    # Set initial state
    board = [["   " for i in range(3)] for _ in range(3)]

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
    print_board(board)

    # Induce loop
    while True:
        # Check whose turn it is
        if whose_turn(board) == player:
            # Get player action and validate
            while True:
                action = input("Select a square from 1 to 9: ")
                # Validate action
                if valid_action(action, board):
                    break
            # Update board with the action
            board = update_board(action, board, player)
            # Check for win or draw:
            if terminal(board):
                return
            else:
                continue
        elif whose_turn(board) == cpu:
            action = choose_action(board, cpu)

            # Let the player know what the CPU chose
            print(f"CPU selects square {action}")
            # Update board with the action
            board = update_board(action, board, cpu)
            # Check for win or draw:
            if terminal(board):
                return
            else:
                continue


# Return a list of all possible actions on the board for the AI to consider
def actions(board: list[list[str]]) -> list[str]:
    legal_actions = []
    for row in board:
        for square in row:
            if square == "   ":
                legal_actions.append(str(board.index(row) * 3 + row.index(square) + 1))
    return legal_actions


# AI selected answer
def choose_action(board: list[list[str]], user_symbol: str) -> str:
    actions_utilities = utility(board, user_symbol)
    return max(actions_utilities.values())


def congratulate_winner(winner: str) -> None:
    print(f"{winner} wins! Congratulations!")


# Check for draw
def draw(board) -> bool:
    if win(board):
        return False
    else:
        for row in board:
            for square in row:
                if square == "   ":
                    return False
        return True


# Print current state of global board
def print_board(board: list[list[str]]) -> None:
    print("Current state:\n")

    for index, row in enumerate(board):
        print("|".join(row))
        if index < 2:
            print("-" * 11)


# Returns the resulting board after a hypothetitcal legal action is taken
def result(board: list[list[str]], action: str, user_symbol: str) -> list[list[str]]:
    row = (int(action) - 1) // 3
    column = (int(action) - 1) % 3

    board[row][column] = user_symbol
    return board


def terminal(board: list[list[str]]) -> bool:
    # Check rows for win
    if win(board) or draw(board):
        return True
    else:
        return False


# Change the board state with the given action by the user
def update_board(action: str, board: list[list[str]], user_symbol: str) -> list[list[str]]:
    # Get the coordinates of the action
    row = (int(action) - 1) // 3
    column = (int(action) - 1) % 3

    # Update the board with the action
    board[row][column] = f" {user_symbol} "

    print_board(board)
    return board


def utility(board: list[list[str]], user_symbol: str) -> dict:
    opponent_symbol = "O" if user_symbol == "X" else "X"
    actions_list = actions(board)
    actions_dict = {key: 0 for key in actions_list}

    # For each possible action, get the resulting utility value, update the dictionary
    for action in actions_dict:
        r = result(board, action, user_symbol)
        if terminal(r):
            if win(r):
                actions_dict[action] = 1
                return actions_dict
            else:
                pass
        else:
            # Now check for opponent's possible actions
            opponent_actions = actions(r)
            for opp_action in opponent_actions:
                r_opp = result(r, opp_action, opponent_symbol)
                if terminal(r_opp):
                    if win(r_opp):
                        actions_dict[action] = -1
                    else:
                        pass
                else:
                    pass
    # The utility of the action is the minimum of the opponent's possible actions
    return actions_dict


# Validate that the action is a number between 1 and 9 and that the square is not already taken
def valid_action(action: str, board:list[list[str]]) -> bool:
    # Check if action is a number between 1 and 9
    if int(action) not in [i for i in range(1, 10)]:
        return False

    # Check if the square is already taken
    row = (int(action) - 1) // 3
    column = (int(action) - 1) % 3

    # if the square is not empty, aka "   ", return False
    if board[row][column] != "   ":
        print("Square already taken.")
        return False

    return True


# Check for win
def win(board: list[list[str]]) -> bool:
    # Check rows for win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "   ":
            return True

    # Check columns for win
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] and board[0][column] != "   ":
            return True

    # Check diagonals for win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "   ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "   ":
        return True

    return False


# Figure out whose turn it is, assuming X always goes first
def whose_turn(board: list[list[str]]) -> str:
    X_count = O_count = 0
    for row in board:
        for square in row:
            if square == " X ":
                X_count += 1
            elif square == " O ":
                O_count += 1

    # compare counts to determine turn
    if X_count == 0:
        return "X"
    elif X_count == O_count:
        return "X"
    elif X_count - 1 == O_count:
        return "O"
    else:
        return "ERROR"


if __name__ == "__main__":
    main()
