import random
count=0
board=[" "," "," "," "," "," "," "," "," "," "]
print("1","|","2","|","3")
print("---------")
print("4", "|", "5", "|", "6")
print("---------")
print("7", "|","8", "|", "9")

#A FUNCTION TO PRINT THE CURRENT POSITION THE BOARD
def showboard():
    print(board[1],"|",board[2],"|",board[3])
    print("---------")
    print(board[4], "|", board[5], "|", board[6])
    print("---------")
    print(board[7], "|", board[8], "|", board[9])

# def check_winner():
#
#     if board[1] == board[2] == board[3] != " ":
#         return 1
#     elif board[4] == board[5] == board[6] != " ":
#         return 1
#     elif board[7] == board[8] == board[9] != " ":
#         return 1
#     elif board[1] == board[4] == board[7] != " ":
#         return 1
#     elif board[2] == board[5] == board[8] != " ":
#         return 1
#     elif board[3] == board[6] == board[9] != " ":
#         return 1
#     elif board[1] == board[5] == board[9] != " ":
#         return 1
#     elif board[3] == board[5] == board[7] != " ":
#         return 1
#     else:
#         pass

#A FUNCTION TO CHECK IF ANYONE HAS WON THE GAME OR NOT
def check_winner():
    i=1
    j=1
    #CHECKING ROW-WISE
    for i in range(1,3):
        if board[i] ==  board[i+1] == board[i+2] != " ":
            return 1

    #CHECKING COLUMN WISE
    for j in range(1,3):
        if board[j] == board[j+3] == board[j+6] != " ":
            return 1

    #CHECKING DIAGONALLY
    if board[1] == board[5] == board[9] != " ":
        return 1

    if board[3] == board[5] == board[7] != " ":
        return 1

#A FUNCTION THAT SELECTS A SPOT FOR THE COMPUTER TO PUT A "O"
def check_my_spot():
    i=1
    j=1
    SpotFound=0

    #CHECKING ROW WISE ,AND IF THERE ARE TOW X'S IN A ROW THAN IT WILL PUT A "O" AT THIRD PLACE
    for i in range(1,3):
        if board[i] == board[i+3] == board[i+6] == " ":
            continue

        elif board[i] == board[i+3] and board[i]!= " ":
            if board[i+6]==" ":
                board[i+6]="o"
                return 1

        elif board[i+3] == board[i+6] and board[i+3]!= " ":
            if board[i]==" ":
                board[i]="o"
                return 1

        elif board[i] == board[i+6] and board[i]!= " ":
            if board[i+3]==" ":
                board[i+3]="o"
                return 1

        else:
            #CHECKING COLUMN WISE , AND IF THERE ARE TOW X'S IN A ROW THEN IT WILL PUT "O" AT THIRD PLACE
            for j in range(1,7,3):

                if board[i] == board[i+1]==board[i+2] == " ":
                    pass

                elif board[i] == board[i+1] and board[i]!= " ":
                    if board[i+2]== " ":
                        board[i+2]="o"
                        return 1

                elif board[i+1] == board[i+2] and board[i+1]!= " ":
                    if board[i] == " ":
                        board[i] = "o"
                        return 1

                elif board[i] == board[i+2] and board[i]!= " ":
                    if board[i+1] == " ":
                        board[i+1] = "o"
                        return 1

                else:
                    pass

    #CHECKING A SPOT IN DIAGONALS
    if board[1]==board[5] and board[1]!=" ":
        if board[9]== " ":
            board[9]="o"
            return 1

    elif board[5]==board[9] and board[5]!=" ":
        if board[1]==" ":
            board[1]="o"
            return 1

    elif board[1]==board[9] and board[1]!=" ":
        if board[5]==" ":
            board[5]="o"
            return 1

    elif board[3] == board[5] and board[3]!=" ":
        if board[7] == " ":
            board[7]="o"
            return 1

    elif board[5]==board[7] and board[5]!=" ":
        if board[3]==" ":
            board[3]="o"
            return 1

    elif board[3]==board[9] and board[3]!=" ":
        if board[5]==" ":
            board[5]="o"
            return 1

    else:
        pass

    #AT LAST ,IT WILL CHOOSE A RANDOM SPOT TO PUT A MARK
    while SpotFound!=1:
        Spot2 = random.randint(1, 9)
        if board[Spot2] != "x" and board[Spot2] != "o":
            board[Spot2] = "o"
            SpotFound=1
            return 1

#A FUNCTION TO CHECK IF THE BOARD IS FULL OR NOT
def is_full(x):
    if x>=9:
        return True
    return False

#MAIN GAME STARTS HERE , ASKING PLAYER 1 TO START FIRST WITH X
while True:
    Spot1=int(input("Please Enter Your Spot :"))

    if board[Spot1] != "x" and board[Spot1] != "o":
        board[Spot1]="x"
        count+=1

        if count>4:
            if check_winner():
                showboard()
                print("Player 1 Won The Game")
                break

        if is_full(count):
            print("The Board is Full Now")
            break

        Spot=check_my_spot()
        count+=1
        print(count)
        # SpotFound=0
        # while SpotFound!=1:
        #
        #     Spot2=random.randint(1,9)
        #
        #     if board[Spot2] != "x" and board[Spot2] != "o":
        #         board[Spot2] = "o"
        #         count+=1
        #         SpotFound=1
        if count>4:
            if check_winner():
                showboard()
                print("Player 2 Won The Game")
                break
    else:
        print("Choose a Diffrent Spot")

    showboard()