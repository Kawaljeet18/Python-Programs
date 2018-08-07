# TO CONSTRUCT A LIST AND REMOVE DUPLICATES FROM IT
# THE PROGRAMS TAKES A LIST AS INPUT FROM THE USER.
# THEN IT REMOVES THE DUPLICATE NUMBERS FROM THE LIST AND REFINE IT FOR DUPLICATES.
# AND THEN GENERATES A NEW LIST.


def get_list():
    a = []
    num = int(input("Please Enter the elements or Press 0 to exit :"))
    while num != 0:
        a.append(num)
        num = int(input("Please Enter Next Element:"))
    return a


def set_list(x):
    return list(set(x))


user_list = get_list()
New_List = set_list(user_list)
print("The User entered list is :", user_list)
print("The System Generated list is :", New_List)

#def Set_list(x):
#   y=[]
#   for i in x:
#       if i not in y:
#           y.append(i)
#   return y