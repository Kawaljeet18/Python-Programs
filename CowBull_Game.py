# COW BULL GAME
# The System Will Generate a Random 4 Digit Number, And the User Has to Guess the number.
# For every Right digit guessed at Right place , Its a COW.
# For Every Right Digit Guessed at Wrong Place , Its a BULL.
# TRY THE GAME , YOU WILL GET IT EASILY
import random


def compare(x,y):
    CowBull = [0,0]
    for i in range(len(x)):
        if x[i] == y[i]:
            CowBull[0] += 1
        elif x[i] in y:
            CowBull[1] += 1
        else:
            pass
    print("Cows = {} Bulls = {}".format(CowBull[0], CowBull[1]))


print("Hi, Lets Start Playing The Cow and Bulls Game :)")
print("I will Generate a 4 Digit Number In The System and You Have To Guess It Right")
print("The Moment You Guess it Right, The Game Will Be Over")
print("Type 'EXIT' if at any time you feel bore!")


user_number = 0
number = str(random.randint(1000,9999))
print(number)


count = 0
while user_number != 'EXIT':
    user_number = input("Please Guess The Number I Generated :")
    if user_number == number:
        count += 1
        print("Yes You Got it !")
        break
    else:
        compare(number,user_number)
    count+=1
if user_number == number:
    print("Guessed it Right On {} attempt :".format(count))