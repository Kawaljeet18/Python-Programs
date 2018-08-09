# TO CHECK THE NUMBER IS PRIME OR NOT
# THE PROGRAM TAKES A NUMBER AS INPUT FROM THE USER THROUGH get_number() function.
# THEN CHECKS WHETHER THE NUMBER IS PRIME OR NOT (check_prime()) AND SAVES THE RESULT IN A VARIABLE.
# TRY THE CODE.


def get_number(msg="Please Enter A number"):
    return int(input(msg))


def check_prime(x):
    if x == 1:
        return 1
    for i in (2,3,5):
        if x%i == 0:
            return 1
            break
    return 0

num = get_number()
code = check_prime(num)
if code == 1:
    print("This Number Is Not A Prime")
else:
    print("It is A Prime Number")
