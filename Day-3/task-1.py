# Each line in the input is a rucksack, with two compartments.
# The first half of the string is the compartment, second compartment is other half.
# Items are letters, lowercase and upper case are different items (a != A)
# Find an item that is in both compartments.
# a - z are given respective numbers 1-26, A - Z are given 27 - 52.

# Find the item type that appears in both compartments of each rucksack, and return the sum.

import string

def readInput():
	data = []
	with open("Day-3/inputs.txt", "r") as file:
		data = file.read().splitlines()

	return data

def main():
	rucksacks = readInput()
	total = 0

	for rucksack in rucksacks:
		comp1 = rucksack[:len(rucksack)//2] # gets first half
		comp2 = rucksack[len(rucksack)//2:] # gets second half

		# Convert both compartments into a set
		comp1Set = set(comp1)
		comp2Set = set(comp2)

		# Find value in both, convert to list for easy reference
		common = list(comp1Set.intersection(comp2Set))

		# Finds the positiion in alphabet, has to be lowered.
		letterVal = string.ascii_lowercase.index(common[0].lower()) + 1
		
		if common[0].isupper():
			letterVal += 26 # If capital, needs to be between 27 - 52
		
		total += letterVal

	print("The sum is:", total)

main()