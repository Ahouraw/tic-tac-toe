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

    cpu = "O" if player == "X" else "X"

    print_board()

    # Induce loop

        # Execute action

        # Check for win or draw:
            # If True, break loop


def print_board():
    print("Current state:\n")
    for index, row in enumerate(board):
        print("|".join(row))
        if index < 2:
            print("-" * 11)


# Figure out whose turn it is, assuming player always goes first
def whose_turn(state):
    player_count = 0
    for row in board:
        for square in row:
            if square == player
                player_count += 1
    return "X" if turn % 2 == 0 else "O"


if __name__ == "__main__":
    main()