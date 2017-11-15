import sys
import random
import itertools
import time


def main():
    current_player = "X"
    turn_tracker = 0

    board = initialize_board()
    print("BEHOLD, YE MIGHTY, AND DESPAIR! PLAY TIC TAC TOE IF YOU DARE!")
    print_board(board)

    if is_versus_ai():
        play_human(board, current_player, turn_tracker)
    else:
        play_ai(board, current_player, turn_tracker)


def is_versus_ai():
    response = input("Play against a computer? Hit the 'y' key ... if you dare: ")

    if response is not "y":
        return False
    else:
        return True


def play_human(board, current_player, turn_tracker):

    while not is_game_over(board, current_player):

        if turn_tracker % 2 == 0:
            current_player = "X"
            prompt_player(board, current_player)
        else:
            current_player = "Y"
            computer_make_move(board, current_player)

        turn_tracker = turn_tracker + 1


def play_ai(board, current_player, turn_tracker):

    while not is_game_over(board, current_player):

        if turn_tracker % 2 == 0:
            current_player = "X"
        else:
            current_player = "Y"

        prompt_player(board, current_player)
        turn_tracker = turn_tracker + 1


def prompt_player(board, current_player):
    coordinates = input("Player " + current_player + ", select an 'x,y' coordinate: ")

    while not is_available_position(coordinates, board):
        print("You must select a valid & unoccupied coordinate.")
        coordinates = input("Try again: ")

    capture_coordinates(coordinates, board, current_player)
    print_board(board)


def is_valid_input(coordinates):

    if coordinates.strip('') == "":
        print("No empty strings allowed!")
        return False

    if not len(coordinates) == 3:
        print("Please enter a conforming input")
        return False

    if not coordinates[0].isdigit() or int(coordinates[0]) < 0 or int(coordinates[0]) > 2:
        print("Select a valid X coordinate between 0,2")
        return False

    if not coordinates[2].isdigit() or int(coordinates[2]) < 0 or int(coordinates[2]) > 2:
        print("Select a valid Y coordinate between 0,2")
        return False

    return True


def is_available_position(coordinates, board):

    if not is_valid_input(coordinates):
        return False
    elif board[int(coordinates[0])][int(coordinates[2])] == ' ':
        return True
    else:
        return False


def capture_coordinates(coordinates, board, current_player):
    board[int(coordinates[0])][int(coordinates[2])] = current_player


def initialize_board():
    return [[' '] * 3 for _ in range(3)]


def print_board(board):

    for row in board:
        for position in row:
            print(position + "|", end=' ')
        print('')


def is_game_over(board, current_player):

    if current_player == board[0][0] == board[0][1] == board[0][2] \
            or current_player == board[1][0] == board[1][1] == board[1][2] \
            or current_player == board[2][0] == board[2][1] == board[2][2] \
            or current_player == board[0][0] == board[1][0] == board[2][0] \
            or current_player == board[0][1] == board[1][1] == board[2][1] \
            or current_player == board[0][2] == board[1][2] == board[2][2] \
            or current_player == board[0][0] == board[1][1] == board[2][2] \
            or current_player == board[0][2] == board[1][1] == board[2][0]:
        print("GAME OVER! PLAYER " + current_player + " WINS!")
        return True

    elif is_draw(board):
        print("IT'S A DRAW!")
        return True
    else:
        return False


def is_draw(board):
    return not any(coordinates == " " for coordinates in itertools.chain(*board))


def computer_make_move(board, current_player):
    choices = []

    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            coordinates = str(row_index) + "," + str(col_index)
            if is_available_position(coordinates, board):
                choices.append(coordinates)

    selected_coordinates = choices[random.randint(0, len(choices) - 1)]
    print("Computer likes to think for three seconds and make its opponent wait...")
    time.sleep(3)
    print("Computer selects: ", selected_coordinates)
    capture_coordinates(selected_coordinates, board, current_player)
    print_board(board)


if __name__ == '__main__':
    sys.exit(main())
