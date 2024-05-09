"""This code is used to return the amount of time in seconds left by a native to use"""

def accept_input():
    """Function that accepts all user's input and also ensure that it clean the input 
    to produce an output needed and useful by other functions"""
    user_input = input("Please enter the starting time: ")
    new_number = 0
    count_a = 0
    count_p = 0
    for i in user_input:
        if i == "a":
            count_a += 1
            new_number = int(user_input[:i])
            if new_number > 12:
                return "Please enter a valid time"
                quit()
        elif i == "p":
            count_p += 1
            print(user_input[i])
            new_number = int(user_input[:i])
            if new_number > 12:
                return "Please enter a valid time"
                quit()
    new_number = int(user_input)
    return new_number, count_a if count_a > 0 else count_p

print(accept_input())


    