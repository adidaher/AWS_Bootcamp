import random
import time

def print_board(board):
    for i, layer in enumerate(board):
        print(f"Layer {i + 1}:")
        for row in layer:
            print(" | ".join(cell if cell != " " else " " for cell in row))
            print("-" * 9)
        print("=" * 9)


def check_win(board, player):
    # Check for horizontal win
    for layer in board:
        for row in layer:
            if all(cell == player for cell in row):
                return True

    for i in range(3):
        for j in range(3):
            if all(board[k][i][j] == player for k in range(3)):
                return True

    if all(board[i][i][i] == player for i in range(3)) or \
       all(board[i][2-i][i] == player for i in range(3)):
        return True

    for layer in board:
        for i in range(3):
            if all(cell == player for cell in layer[i]):
                return True
        if all(layer[i][i] == player for i in range(3)) or \
           all(layer[i][2-i] == player for i in range(3)):
            return True

    return False

def check_tie(board):
    return all(all(cell != " " for cell in row) for layer in board for row in layer)

def make_move(board, player, player1, player2):
    while True:
        try:
            print(f"{player}'s turn")
            x, y, z = map(int, input("Enter your move (layer, row, column): ").split())
            if board[x][y][z] == " ":
                board[x][y][z] = "X" if player == player1 else "O"
                break
            else:
                print("That position is already taken. Try again.")
        except ValueError:
            print("Invalid input. Please enter three integers separated by spaces.")
        except IndexError:
            print("Invalid input. Please enter values within the range.")

def switch_player(current_player):
    return "X" if current_player == "O" else "O"

def reset_game():
    return [[[ " " for _ in range(3)] for _ in range(3)] for _ in range(3)]
def main():
    print("Welcome to 3D Triple Decker Tic-Tac-Toe!")
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")
    current_player = random.choice([player1, player2])
    board = reset_game()

    while True:
        print_board(board)
        make_move(board, current_player, player1, player2)  # Pass player1 and player2 as arguments
        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! {current_player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        else:
            current_player = player1 if current_player == player2 else player2

        time.sleep(1)  # Optional: Add a delay between moves for better visualization

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        main()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    main()
