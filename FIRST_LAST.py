# Create a new list with first and last element of user input List
# THE PROGRAMS TAKES A LIST AS AN INPUT FROM THE USER.
# THEN IT DETERMINES THE FIRST AND LAST ELEMENT OF THE USER ENTERED LIST AND CREATES A NEW LIST.
# A SIMPLE BUT VERY USEFUL.
def get_list():
    x=int(input("Enter the list elements or press 0 to exit:"))
    a=[]
    while x!=0:
        a.append(x)
        x=int(input("Enter The Next Element :"))
    return a
def new_list(a):
    b=[]
    b.append(a[0])
    b.append(a[-1])
    return b
My_list=get_list()
print("The New list is" ,new_list(My_list))



