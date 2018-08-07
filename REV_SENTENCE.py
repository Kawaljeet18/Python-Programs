# TO REVERSE THE STRING ENTERED BY THE USER
# THE USER ENTERS A SENTENCE AS ASKED BY THE PROGRAM
# THE PROGRAM SPLITS THE SENTENCE AND THEN REVERSES IT AS A RESULT.
# THE SENTENCE IS THE JOINED .


def get_string():
    return input("Please Enter A Sentence:")


def rev(x):
    new = x.split()
    new.reverse()
    return new


new_string = str(get_string())
reverse_string = rev(new_string)
print("The User Entered {}".format(new_string))
print("The Reverse Of Above string is :"," ".join(reverse_string))

#one liner solution
#return " ".join(string(split)[::-1])