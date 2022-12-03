# Every 3 lines is a group of elves.
# Each group has a shared item, following the same rules as before.
# The value for that shared item is the group badge.

# Find the sum of all group badges.

import string

def readInput():
	data = []
	with open("Day-3/inputs.txt", "r") as file:
		data = file.read().splitlines()

	return data

def main():
	rucksacks = readInput()
	total = 0

	for r in range(0, len(rucksacks)-1, 3):
		rucksack1 = rucksacks[r]
		rucksack2 = rucksacks[r+1]
		rucksack3 = rucksacks[r+2]

		# Convert rucksacks into sets
		r1Set = set(rucksack1)
		r2Set = set(rucksack2)
		r3Set = set(rucksack3)

		# Find the value in all 3 sets, converted to list for east reference
		common = list(r1Set.intersection(r2Set, r3Set))

		# Finds the positiion in alphabet, has to be lowered.
		letterVal = string.ascii_lowercase.index(common[0].lower()) + 1

		if common[0].isupper():
			letterVal += 26 # If capital, needs to be between 27 - 52

		total += letterVal

	print("The sum is:", total)

main()