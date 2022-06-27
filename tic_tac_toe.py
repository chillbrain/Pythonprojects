def print_board(pos):
    print(str(pos[1]) + " | " + str(pos[2]) + " | " + str(pos[3]))
    print("----------")
    print(str(pos[4]) + " | " + str(pos[5]) + " | " + str(pos[6]))
    print("----------")
    print(str(pos[7]) + " | " + str(pos[8]) + " | " + str(pos[9]))


def who_plays_first(attempt):
    player = ["X", "O"]
    player[0] = input(" what letter do you want to be X or O : ").upper()
    if player[0] == "X":
        player[1] = "O"
        print("Player 1 = X and Player 2 = 0 ")
        GameOn(player)
    elif player[0] == "O":
        player[1] = "X"
        print("Player 1 = O and Player 2 = X ")
        GameOn(player)
    else:
        print(" Invalid input. Enter alphabets only - X or O ")
        if attempt < 3:
            attempt = attempt + 1
            who_plays_first(attempt)

        else:
            print(" Invalid input for 3 attempts. Exiting Game. Good Bye !!")
            exit(1)


def GameOn(player):
    counter = 1
    game = True
    while game:
            for i in range(0, 2):
                move = input("Player{} : Enter the number on the board ".format(i + 1))
                pos[int(move)] = player[i]
                counter = counter + 1
                print_board(pos)
                game = check_status(pos, player[i])
                print(counter)
                if (not game) and (counter <= 10) :
                    again = input("Player{} wins !!\n Do you want to play again Enter Y or N".format(i + 1))
                    replay(again)
                elif counter >= 10:
                    again = input("This game is DRAW \n Do you want to play again Enter Y or N")
                    replay(again)
                continue


def check_status(board, le):
    if ((board[7] == le and board[8] == le and board[9] == le) or
            (board[4] == le and board[5] == le and board[6] == le) or
            (board[1] == le and board[2] == le and board[3] == le) or
            (board[1] == le and board[4] == le and board[7] == le) or
            (board[8] == le and board[5] == le and board[2] == le) or
            (board[9] == le and board[6] == le and board[3] == le) or
            (board[7] == le and board[5] == le and board[3] == le) or
            (board[1] == le and board[5] == le and board[9] == le)):
        return False
    else:
        return True


def replay(again):
    global pos
    if again.upper() == "Y":
        pos = []
        attempt = 0
        for i in range(0, 10):
            pos.append(i)
        print_board(pos)
        who_plays_first(attempt)
    else:
        print("Good Bye !!")
        exit(0)


print("WELCOME to TIC TAC TOE")
again = "y"
replay(again)

