import random
from IPython.display import clear_output

def display_board(board):
    row1 = [board[0],board[1],board[2]]
    row2 = [board[3],board[4],board[5]]
    row3 = [board[6],board[7],board[8]]

    print(row1)
    print(row2)
    print(row3)

def player_input():
    p_input = False

    while p_input == False:
        marker = input('Would you like to be X or O :')
        if (marker.lower())[0] in ['x','o']:
            p_input = True
            return marker.upper()
        else:
            clear_output()

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board, mark):
    win = False

    if board[0] == mark and board[1] == mark and board[2] == mark:
        win = True
    elif board[0] == mark and board[3] == mark and board[6] == mark:
        win = True
    elif board[0] == mark and board[4] == mark and board[8] == mark:
        win = True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        win = True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        win = True
    elif board[2] == mark and board[4] == mark and board[6] == mark:
        win = True
    elif board[3] == mark and board[4] == mark and board[5] == mark:
        win = True
    elif board[6] == mark and board[7] == mark and board[8] == mark:
        win = True

    return win


def choose_first():
    first_player = random.randint(1,2)
    print(f'Player {first_player} goes first')
    return first_player

def space_check(board, position):
    return board[position].lower() not in ['x','o']

def full_board_check(board):
    if '#' in board:
        return False
    else:
        return True

def player_choice(board):
    choice = False

    while choice == False:
        p_choice = input('What position do you want (1 - 9):')

        if p_choice in str(list(range(1,10))):
                i_choice = int(p_choice) - 1
                if space_check(board, i_choice):
                    choice = True
                    return i_choice
        else:
            clear_output()
            print('Space not FREE!!!')
            display_board(board)

def replay():
    play = False

    while play == False:
        play_input = input('Would you like to play again? (Y or N) :')
        if (play_input.lower())[0] in ['y','n']:
            play = True
            if (play_input.lower())[0] == 'y':
                return True
            else:
                return False
        else:
            clear_output()


game = True

while game == True:
    print('Welcome to Tic Tac Toe!')
    print('')

    current_board = ['#','#','#','#','#','#','#','#','#']
    numbered_board = list(range(1,10))
    counter = 0

    display_board(current_board)
    print('')
    display_board(numbered_board)
    print('')

    first = choose_first()
    if first == 1:
        second = 2
    else:
        second = 1

    player_marker = player_input()
    if player_marker == 'X':
        other_player_marker = 'O'
    else:
        other_player_marker = 'X'

    clear_output()
    print(f'Player {first} is {player_marker} and Player {second} is {other_player_marker}')
    print('')
    display_board(current_board)
    print('')
    display_board(numbered_board)
    print('')


    while full_board_check(current_board) == False and win_check(current_board,player_marker) == False:
        if counter % 2 == 0:
            clear_output()
            display_board(current_board)
            print('')
            print(f'{player_marker} it is your turn')
            place_marker(current_board,player_marker,player_choice(current_board))
            counter = counter + 1
        else:
            clear_output()
            display_board(current_board)
            print('')
            print(f'{other_player_marker} it is your turn')
            place_marker(current_board,other_player_marker,player_choice(current_board))
            counter = counter + 1



    if full_board_check(current_board) == True:
        print(f'The board is FULL!')
    if win_check(current_board,player_marker) == True:
        if counter % 2 != 0:
            print(f'{player_marker} wins, well done player {first}')
            display_board(current_board)
        else:
            print(f'{other_player_marker} wins, well done player {second}')
            display_board(current_board)

    game = replay()
