# FINDING AN ELEMENT USING BINARY SEARCH
# USING BINARY SEARCH TO FIND AN ELEMENT.


def binary_search(x, user_list):
    start_index = 0
    end_index = len(user_list)

    while True:
        middle_index = int((end_index-start_index)/2)
        if middle_index > end_index or middle_index < start_index or middle_index < 0:
            return False

        middle_element = user_list[middle_index]
        if x == middle_element:
            return True
        elif x > middle_element:
            start_index = middle_index
        else:
            end_index = middle_index


user_list = [1, 5, 8, 9, 6, 7, 15, 67, 98, 36, 84, 56, 12, 48, 78, 34, 76, 59, 31, 94, 63, 57, 92, 51, 68, 33, 44, 82]
user_list.sort()
print(user_list)

Number = int(input("Please Enter the Number to Search in the Above list : "))
boolean = binary_search(Number,user_list)
if boolean:
    print("The Element is in the list.")
else:
    print("The Element is not in the list.")