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
        # Execute action
        if whose_turn() == player:
            while True:
                action = input("Select a square from 1 to 9: ")
                # Validate action
                if valid_action(action):
                    break
                else:
                    print("Invalid action.")
            # Update board
            update_board(action, player)
            if win_or_draw():
                break
        # Check for win or draw:
            # If True, break loop


# Print current state of global board
def print_board():
    print("Current state:\n")
    for index, row in enumerate(board):
        print("|".join(row))
        if index < 2:
            print("-" * 11)


# Figure out whose turn it is, assuming X always goes first
def whose_turn():
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
    

def valid_action(action):
    ... # TODO


def update_board(action, player):
    ... # TODO


def win_or_draw():
    ... # TODO

if __name__ == "__main__":
    main()