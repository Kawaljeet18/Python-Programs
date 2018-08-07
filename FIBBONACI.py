# TO PRINT THE FIBBONACI SERIES AS PER THE USER INPUT
# THE PROGRAM TAKES THE LENGTH OF THE FIBBONACI SERIES FROM THE USER
# THEN IT PRINTS THE DESIRED RESULT

def get_input(text="Please Enter the length of fibbonaci series :"):
    return int(input(text))

def get_series(length):
    a=0
    b=1
    num=0
    i=0
    fib=[]
    for i in range(0,length):
        fib.append(num)
        num=a+b
        a=num
        b=fib[-1]

    return fib
Len=get_input()
print("The Fibnocci series is :",get_series(Len))
