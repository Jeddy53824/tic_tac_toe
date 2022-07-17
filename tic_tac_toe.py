the_board={}
the_board.update({"7":" ", "8":" ", "9":" ", "4":" ", "5":" ", "6":" ", "1":" ", "2":" ", "3":" "})

board_keys = []

for key in the_board:
    board_keys.append(key)

def show_board(board):
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])

#show_board(the_board)

def game():
    turn = "X"
    count = 0

    for i in range(10):
        show_board(the_board)
        print("It's " + turn + "'s turn. Pick your square.")
        
        move = input()
        if the_board[move] == " ":
            the_board[move] = turn
            count +=1
        else:
            print("That place is taken. Pick again.")
            continue
        if count >=5:
            if the_board["7"] == the_board["8"] == the_board["9"] != " ":
                show_board(the_board)
                print(turn + " wins!!")
                print("GAME OVER")
                break
            elif the_board["4"] == the_board["5"] == the_board["6"] != " ":
                show_board(the_board)
                print(turn + " wins!!")
                print("GAME OVER")
                break
            elif the_board["1"] == the_board["2"] == the_board["3"] != " ":
                show_board(the_board)
                print(turn + " wins!!")
                print("GAME OVER")
                break
            elif the_board["7"] == the_board["4"] == the_board["1"] != " ":
                show_board(the_board)
                print(turn + " wins!!")
                print("GAME OVER")
                break
            elif the_board["8"] == the_board["5"] == the_board["2"] != " ":
                show_board(the_board)
                print(turn + " wins!!")
                print("GAME OVER")
                break
            elif the_board["9"] == the_board["6"] == the_board["3"] != " ":
                show_board(the_board)
                print(turn + " wins!!")
                print("GAME OVER")
                break
            elif the_board["7"] == the_board["5"] == the_board["3"] != " ":
                show_board(the_board)
                print(turn + " wins!!")
                print("GAME OVER")
                break
            elif the_board["9"] == the_board["5"] == the_board["1"] != " ":
                show_board(the_board)
                print(turn + " wins!!")
                print("GAME OVER")
                break
        if count == 9:
            show_board(the_board)
            print("It's a tie!")
            print("GAME OVER")
            break
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    restart = input("Do you want to play again?")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            the_board[key] = " "
        game()
    
game()