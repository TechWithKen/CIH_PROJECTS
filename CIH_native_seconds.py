"""This code is used to return the amount of time in seconds left by a native to use"""

def accept_input():
    """Function that accepts all user's input and also ensure that it clean the input to produce an output needed and useful by other functions"""
    user_starting_time = input("Please enter the starting time: ")
    amount_of_natives = int(input("Please enter the amount of natives available: "))
    return [user_starting_time, amount_of_natives]

def extract_starting_time_as_integer(starting_time):
	"""Function to calculate the amount in seconds used by individual natives in the community innovation hub."""
	count_a = 0
	count_p = 0
	status = 0
	for i in range(len(starting_time)):
		if starting_time[i].lower() == "a":
			count_a += 1
			status = starting_time[:-1]
		else:
			count_p += 1
			status = (starting_time[:i-1])
		
	return int(status) if count_a > 0 else int(status) + 12 if int(status) < 12 else int(status)

time_as_number = extract_starting_time_as_integer(accept_input()[0])

def seconds_for_each_natives(time_to_start, number_of_natives):
	"""This function helps in calculating the total seconds used by each native"""
	closing_time = 16
	time_spent = closing_time - time_to_start
	time_in_seconds = time_spent * 60 * 60
	secs_used_by_one_native = time_in_seconds / number_of_natives

	return f"With the starting time of {accept_input()[0]} today, the time used by {number_of_natives} natives each is {int(secs_used_by_one_native)} seconds"

print(seconds_for_each_natives(time_as_number,accept_input()[1]))
