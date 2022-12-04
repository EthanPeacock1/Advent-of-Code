# They now want to know the pairs with any overlap.

def readInput():
	pairs = []
	with open("Day-4/inputs.txt", "r") as file:
		pairs = [line.strip("\n").split(",") for line in file]

	return pairs

def main():
	total = 0
	pairs = readInput()

	for pair in pairs:
		elf1 = pair[0].split("-")
		elf2 = pair[1].split("-")

		# Fill out all numbers for the given Elf's range
		e1Sections = [s for s in range(int(elf1[0]), int(elf1[1])+1)]
		e2Sections = [s for s in range(int(elf2[0]), int(elf2[1])+1)]

		# Turn into a set, to use set operations
		e1Set = set(e1Sections)
		e2Set = set(e2Sections)

		if (e1Set.isdisjoint(e2Set) == False): # disjoint means they share nothing
			total += 1

	print("Pairs that fully contain each other:", total)

main()