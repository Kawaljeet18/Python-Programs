# The Hangman Game , Guess The Word Selected By Computer
# THE PROGRAM WILL RANDOMLY SELECT A WORD FROM SOWPODS.TXT FILE CONTAINING WORDS.
# THEN IT WILL TELL YOU THE LENGTH OF THE WORD IT SELECTED FROM THE DICTIONARY( THE ONLY HINT FOR YOU)
# THEN IT ASKS YOU TO GUESS THE WORD IN 6 ATTEMPTS.
# QUITE A DIFFICULT GAME, TRY IT YOURSELF.

import random
Guess_Count = 0
# A FUNCTION TO CHECK WHETHER THE USER IS SUCCESSFUL OR NOT IN GUESSSING THE WORD


def check_match(Guess_Word):
    for i in range(0, length):
        if Guess_Word[i] != Word[i]:
            return 5
    return 1

# A FUNCTION TO CHECK ,WHETHER MORE CHANCES ARE AVAILABLE OR NOT


def chances_over(x):
    if x == 6:
        return 1


# OPENING A FILE , THAT CONTAINS A LIST OF WORDS , FROM WHICH WE WILL RANDOMLY PICK A WORD
with open("sowpods.txt", 'r') as rf:
    content = rf.readlines()
    Word = random.choice(content)
    length = len(Word.strip())

# print(Word) , IF YOU WANT TO SEE THE WORD SELECTED BY THE PROGRAM
# CREATING A STRING WITH "-" AS ITS CONTENTS WHICH IS EQUAL IN LENGTH AS THE WORD SELECTED BY PROGRAM.

User_Guess = []
for i in range(0,length):
    User_Guess.insert(i, "-")

# ASKING THE USER , WHETHER HE IS INTERSTED IN PLAYING THE GAME OR NOT.
GamePlay=input("I Am Thinking About A Word in My Mind, Can You Guess It Right ? Y or N ? :")
if GamePlay == "Y" or GamePlay == "y":
    print("=====================================================================")
    print("Hey Buddy You Have Got 6 Chances to Get It Right , So All The Best :)")
    print("=====================================================================")
    print("Let Me Tell You , Its A {} Letters Word".format(length))

# HERE IS THE MAIN PROGRAM THAT INITIATES THE GAME FOR THE USER AFTER HE AGREES TO PLAY IT.
# THE GAME WILL EXIT AS SOON AS THE USER GUESS THE WORD CORRECTLY OR WHEN THE MAX. CHANCES ARE OVER I.E. 6

    while True:
        Game = chances_over(Guess_Count)
        if Game == 1:
            print("YOU RAN OUT THE THE MAXIMUM CHANCES ALLOWED, SORRY ! ")
            print("THE WORD I SELECTED WAS : {}".format(Word))
            break
        print("=====================================================================")
        letter = input("Please Make Your {} Guess :".format(Guess_Count+1))
        Guess_Count += 1
        letter = letter.upper()
        # CHECKING THE OCCURRENCE OF THE USER GUESSED LETTER IN THE PROGRAM SELECTED WORD
        # FOR EVERY OCCURRENCE IT WILL REPLACE "-" WITH THE LETTER AT SAME PLACE

        for i in range(len(Word)):
            if letter == Word[i]:
                User_Guess[i] = Word[i]

        # CONVERTING THE USER_LIST TO A STRING
        Match_Word = "".join(User_Guess)
        Letter_Left = User_Guess.count("-")
        print(Match_Word)

        # ASKING THE USER WHETHER HE CAN GUESS THE COMPLETE WORD .
        opinion = input("Can You Guess The Complete Word Now? Y or N :")
        if opinion == "Y" or opinion == "y":
            Complete_Guess = input("OK, What You Think It Is : ")
            Result = check_match(Complete_Guess.upper())

            if Result == 1:
                print("OH ! You Have Guessed it Right Man ,Cheers :)")
                break
            else:
                print("Oops, It Was Not A Perfect Shot.")
        else:

            Result = check_match(Match_Word)
            if Result == 1:
                print("OH ! You Have Guessed it Right Man ,Cheers :)")
                break


else:
    print("No Issue , Happy To Meet You :)")