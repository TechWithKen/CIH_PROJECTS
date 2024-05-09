"""This code is used to pluralise a given word"""

def pluralise(word: str):
	"""This function is used to return the plural of a word"""
	vowel_sounds = ["a", "e", "i", "o", "u"]
	if word[len(word) - 2] in vowel_sounds and word[-1] != 's':
		plural = word + 's'
		return f'The plural of the word {word} is {plural}'

	elif word[-1] == 's':
		second_plural = word + "'"
		return f"The plural of the word {word} is {word} but if it's a name, the plural is {second_plural}"

	elif word[-1] == 'y':
		third_plural = word[:(len(word) -1)] + "ies"
		return f'The plural of the word {word} is {third_plural}'

	elif word[len(word) - 2:] == "fe":
		fourth_plural = word[:(len(word) -2)] + "ves"
		return f'The plural of the word {word} is {fourth_plural}'

	else:
		new_plural = word + "s"
		return f'The plural of the word {word} is {new_plural}'

while True:
	user_input = input("Enter any word you want: ")
	print(pluralise(user_input))
	again = input("Do you want to try again:(y/n)->")
	if again.lower() == "y":
		continue
	else:
		print("Thank you for trying")
		break