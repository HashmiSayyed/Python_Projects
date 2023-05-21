import random


def display_board(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[1] + "|" + board[2] + "|" + board[3])


def player_input():
    marker = ""

    while not (marker == "X" or marker == "O"):
        marker = input("Do you want X or O: ").upper()

    if marker == "x":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, marker):
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[7] == marker and board[4] == marker and board[1] == marker) or
            (board[8] == marker and board[5] == marker and board[2] == marker) or
            (board[9] == marker and board[6] == marker and board[3] == marker) or
            (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[3] == marker and board[5] == marker and board[7] == marker))


def choose_first():
    if random.randint(0, 1) == 0:
        return "Player-1"
    else:
        return "Player-2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose next position: "))

    return position


def replay():
    return input("Want to play again? Y or N: ").lower().startswith("y")


print("Tic Tac Toe")

while True:
    theBoard = [" "] * 10
    player_1_marker, player_2_marker = player_input()
    turn = choose_first()
    print(f"{turn} will go first.")

    play_game = input("Ready to play? y or n: ")
    if play_game.lower() == "y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player-1":
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player_1_marker, position)

            if win_check(theBoard, player_1_marker):
                display_board(theBoard)
                print("Player 1 wins.")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("Game is draw.")
                    break
                else:
                    turn = "Player-2"

        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player_2_marker, position)

            if win_check(theBoard, player_2_marker):
                display_board(theBoard)
                print("Player 2 wins.")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("Game is draw.")
                    break
                else:
                    turn = "Player-1"

    if not replay():
        break
