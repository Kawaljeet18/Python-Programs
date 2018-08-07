#When will you turn 100
import datetime
Name=input("Please Enter Your Name")
Age=int(input("Please Enter Your Age"))
Temp=100-Age
Now=datetime.datetime.now()
print("Current Year :",Now.year)
Year=Now.year+Temp
print("You Will Turn 100 in :",Year)