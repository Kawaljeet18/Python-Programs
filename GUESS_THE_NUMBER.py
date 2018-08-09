# To GUESS THE NUMBER IN USER'S MIND
# THE PROGRAMS ASKS YOU TO THINK A NUMBER BETWEEN 1-500 IN YOUR MIND
# AFTER YOU DECIDED YOUR NUMBER THEN PRESS ENTER
# IT WILL GUESS YOUR NUMBER RANDOMLY
# THEN IT WILL ASK IF THE NUMBER GUESSED WAS LOWER OR HIGHER THAN YOUR NUMBER
# IT WILL TRY TO CUT ITS RANGE UNLIT IT FINDS YOUR NUMBER .
# THE CODE NEED SOME UPDATE BUT TRY THIS PLEASE, ITS INTERESTING.


import random
input("Please Think of a number between 1-500 and Press Enter !")
first = 1
last = 500
count = 1
UserInput = 0

while UserInput != "y" or UserInput != "Y":
    # print(first,last)
    Guess = random.randint(first,last)
    UserInput = input("Are You Thinking of {} , Y or N ?".format(Guess))
    if UserInput == "N" or UserInput=="n":
        Opinion = input("Did I Guessed It Higher Than Yours? , Y or N ?")
        if Opinion == "Y" or Opinion == "y":
            last = Guess
        else:
            first = Guess
    else:
        print("Yupiieee, I Got it :)")
        break
    count += 1

print("{} Attempts ".format(count))