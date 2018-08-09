# TO SCAN TWO FILES I.E PRIME_NUMBERS AND HAPPY_NUMBERS AND FIND THE NUMBERS OVERLAPPING AND STORE THEM INTO A LIST.
# THIS PROGRAMS IS WORKING ON TWO FILES
# THE FIRST FILE CONTAINS THE NUMBERS THAT ARE PRIME, AND THE SECOND FILE CONTAINS HAPPY NUMBERS.
# IT CHECKS BOTH THE FILES AND CHOOSE THE NUMBERS THAT ARE COMMON TO BOTH THE FILES I.E PRIME AND HAPPY.
# AND THEN STORES THESE NUMBERS IN A NEW LIST CALLED OverlappingNumbers.


count = 0
OverlappingNumbers = []
with open("Prime_number.txt", 'r') as first:
    reader1 = first.read()
    with open("Happy_number.txt", 'r') as second:
        reader2 = second.readlines()
        for line in reader2:
            if line in reader1:
                OverlappingNumbers.append(int(line))
                count += 1

print("{} Numbers are overlapping".format(count))
print("The List Contains", OverlappingNumbers)