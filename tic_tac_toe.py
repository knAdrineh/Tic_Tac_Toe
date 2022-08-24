#Adrineh Khodaverdian
import random


def display_board(board):
    if len(board) == 10:
        for i in range(1,10):
            if i%3 != 0:
                print(f" {board[i]} | ", end="")
            else:
                if i != 9:
                    print(f" {board[i]} \n-------------")
                else:
                    print(f" {board[i]}")
def player_input():
    player_sign = 'P'
    while player_sign.upper() not in['X', 'O']:
        player_sign = input("Please pick a marker 'X' or 'O' : ")
        player_sign = player_sign.upper()
    player1 = player_sign
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return player1,player2

def place_marker(board, marker, position):
    while board[position] != '':
        print("Position is already filled, please use another spot ")
        position = int(input("Input empty position 1-9 : "))
    if board[position] == '':
        board[position] = marker


def win_check(board, mark):
    iswinner = False
    # checking the rows
    if board[1] == board[2] == board[3] == mark or \
            board[4] == board[5] == board[6]== mark or \
            board[7] == board[8] == board[9]== mark or \
            board[1] == board[4] == board[7]== mark or \
            board[2] == board[5] == board[8]== mark or \
            board[3] == board[6] == board[9]== mark or\
            board[1] == board[5] == board[9]== mark or\
            board[3] == board[5] == board[7]== mark:
        iswinner = True
    else:
        iswinner = False

    return iswinner


def choose_first():
    rand_num = random.randint(1, 11)
    if rand_num % 2 == 0:
        return 'X'
    else:
        return 'O'

def space_check(board, position):
    return board[position]==''

def full_board_check(board):
    count_space = 0
    for i in range(1, len(board)):
        if space_check(board, i):
            count_space += 1

    return count_space == 0


def player_choice(board):
    next_pos = int(input("Enter a number between 1-9 : "))
    while next_pos not in range(1, 10) and not space_check(board,next_pos):
        next_pos = int(input("Enter a number between 1-9 : "))

    return next_pos

def replay():
    choice = 'wrong'
    rep = False
    while choice.upper() not in ['Y','N']:
        choice = input("Would you like to play again ? (Y | N) \n")
    return choice.upper() == 'Y'

def main():
    print('Welcome to Tic Tac Toe!')

    is_done = False
    restart = 'Y'


    while restart.upper() !='N' or restart.upper() == 'Y':
        board = ['#', '', '', '', '', '', '', '', '', '']
        player1, player2 = player_input()
        first = choose_first()
        if player1 == first:
            print(f"{first} starts the game.")
        else:
            print(f"wait for {first} to start the game.")
        is_done = False
        while not is_done :
            print (f"player {first}, ",end="")
            pos = player_choice(board)
            place_marker(board,first,pos)
            display_board(board)
            # change turn


            if win_check(board, first):
                print(f"Congrats {first} you won the game ! ")
                is_done = True


            elif full_board_check(board) and not win_check(board, first) :
                print("Game Over!\n It's a Tie!")
                is_done = True


            if player1 == first:
                first = player2
            else:
                first = player1
        again  = replay()
        if again == True:
            restart = 'Y'
        elif again == False:
            restart = 'N'




main()