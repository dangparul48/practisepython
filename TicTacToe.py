import random


def print_board(board):
    print()
    print("Game board \t\t Help board")
    print(f'{board[1]}|{board[2]}|{board[3]} \t\t\t 1|2|3')
    print('-+-+- \t\t\t -+-+-')
    print(f'{board[4]}|{board[5]}|{board[6]} \t\t\t 4|5|6')
    print('-+-+- \t\t\t -+-+-')
    print(f'{board[7]}|{board[8]}|{board[9]} \t\t\t 7|8|9')


def check_winning_combinations(board):
    somebody_won, who_won = False, " "
    if board[1] == board[2] == board[3] != " ":
        somebody_won, who_won = True, board[1]
    elif board[4] == board[5] == board[6] != " ":
        somebody_won, who_won = True, board[4]
    elif board[7] == board[8] == board[9] != " ":
        somebody_won, who_won = True, board[7]
    elif board[1] == board[4] == board[7] != " ":
        somebody_won, who_won = True, board[1]
    elif board[2] == board[5] == board[8] != " ":
        somebody_won, who_won = True, board[2]
    elif board[3] == board[6] == board[9] != " ":
        somebody_won, who_won = True, board[3]
    elif board[1] == board[5] == board[9] != " ":
        somebody_won, who_won = True, board[1]
    elif board[3] == board[5] == board[7] != " ":
        somebody_won, who_won = True, board[3]
    return somebody_won, who_won


board = {}
for i in range(1, 10):
    board[i] = " "

print("Welcome to Tic Tac Toe game")
print("Rules of the game---")
print("1. Choose among yourself about your symbols i.e. O or X")
print("2. There are nine boxes in the board")
print("3. You will have to enter your box number on your turn")
print("4. Boxes number start from 1")
print("5. Board looks like as below")
print_board(board)

turn = ""
choices = ["X", "O"]
turn = choices[random.randint(1, 2)-1]
turncount = 0

while turncount < 9:
    print()
    box = int(input("Turn of " + turn + ". Enter your box number: "))
    if box not in board:
        print("Invalid choice")
        pass
    elif board[box] != " ":
        print(f'Invalid choice. {box} number box is already filled')
        pass

    turncount += 1
    board[box] = turn
    print_board(board)
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

    somebody_won, who_won = check_winning_combinations(board)
    if somebody_won:
        print(f'\nCongratulations, {who_won} won.')
        break

    if turncount == 9:
        print("\nTough game. Nobody won.")
