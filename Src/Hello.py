def user_marker():
    marker_list = ['x','o']
    player_marker = input("Player1 choose the marker 'X' or 'O'\n")

    if player_marker == marker_list[0]:
        marker = {'player1_marker': marker_list[0], 'player2_marker': marker_list[1]}
        print("Player1 choose {}".format(marker_list[0]))
        print("Player2 choose {}\n\n".format(marker_list[1]))
    elif player_marker == marker_list[1]:
        marker = {'player1_marker': marker_list[1], 'player2_marker': marker_list[0]}
        print("Player1 choose {}".format(marker_list[1]))
        print("Player2 choose {}\n\n".format(marker_list[0]))
    else:
        print("Chosen marker not Allowed")

    return marker

def game_launch(kwargs):
    row1 = [' ', ' ', ' ']
    row2 = [' ', ' ', ' ']
    row3 = [' ', ' ', ' ']
    check_list = []

    print("Choose a number between 1-9 as pos on board\n")
    game_on = 9
    start_player = 'player1'
    next_player  = 'player2'
    current_player = start_player
    while game_on >=1:
        if current_player == start_player:
            board_pos_player1 = input("Player1 turn\n")
            turn = display (row1,row2,row3,board_pos_player1,kwargs['player1_marker'],check_list,current_player)
            if turn == current_player:
                current_player = current_player
            else:
                game_on -= 1
                current_player = next_player
        elif current_player == next_player:
            board_pos_player2 = input("Player2 turn\n")
            turn = display(row1,row2,row3,board_pos_player2, kwargs['player2_marker'],check_list,current_player)
            if turn == current_player:
                current_player = current_player
            else:
                game_on -= 1
                current_player = start_player
    if game_on < 1:
        print("No one Wins\n")
        restart_game = input ("Do you want to restart game 'y' \ 'n' \n")
        if restart_game == 'y':
            game_init()
        else:
            exit()

def display(row1,row2,row3,pos,kwargs,check_list,current_player):

    if int(pos) in check_list:
        print ("Already chosen, Select different position\n")
        return current_player
    else:
        if pos == '1':
            row1[0] = kwargs
        elif pos == '2':
            row1[1] = kwargs
        elif pos == '3':
            row1[2] = kwargs
        elif pos == '4':
            row2[0] = kwargs
        elif pos == '5':
            row2[1] = kwargs
        elif pos == '6':
            row2[2] = kwargs
        elif pos == '7':
            row3[0] = kwargs
        elif pos == '8':
            row3[1] = kwargs
        elif pos == '9':
            row3[2] = kwargs

    check_list.append(int(pos))

    print(row3[0] + "|" + row3[1] + '|' + row3[2])
    print(row2[0] + "|" + row2[1] + '|' + row2[2])
    print(row1[0] + "|" + row1[1] + '|' + row1[2])

    is_winner = winner_check(row1,row2,row3,kwargs)

    if is_winner:
        restart_game = input ("Do you want to restart game 'y' \ 'n' \n")
        if restart_game == 'y':
            game_init()
        else:
            exit()


def winner_check(row1,row2,row3,kwargs):

    if row1[0] == row1[1] == row1[2] == kwargs \
    or row2[0] == row2[1] == row2[2] == kwargs \
    or row3[0] == row3[1] == row3[2] == kwargs \
    or row1[0] == row2[1] == row3[2] == kwargs \
    or row1[0] == row2[0] == row3[0] == kwargs \
    or row1[1] == row2[1] == row3[1] == kwargs \
    or row1[2] == row2[2] == row3[2] == kwargs \
    or row3[0] == row2[1] == row1[2] == kwargs:
        print ("{} wins the game\n".format(kwargs))
        return True
    else:
        return False



def game_init():
    print("*** Welcome to Tic Tac Toe ***\n")
    marker = user_marker()
    print("Game Begins")
    game_launch(marker)



def main():
    game_init()

if __name__ == "__main__":
    main()