# The ship has some reamining stacks of marked crates which need to be rearranged.
# Using a giant cargo crane, crates will be rearranged in a series of carefully planned steps.
# After rearranging, the desired crates will be at the top of each stack.
# CRATES ARE MOVED ONE BY ONE

# The input is the rearrangement procedure.
# The Evles want to know which crate will end up on top of each stack.

stack = [ # OLD method of implementing the stack, to run the code remove the stack from inputs file
	["D", "H", "N", "Q", "T", "W", "V", "B"],
	["D", "W", "B"],
	["T", "S", "Q", "W", "J", "C"],
	["F", "J", "R", "N", "Z", "T", "P"],
	["G", "P", "V", "J", "M", "S", "T"],
	["B", "W", "F", "T", "N"],
	["B", "L", "D", "Q", "F", "H", "V", "N"],
	["H", "P", "F", "R"],
	["Z", "S", "M", "B", "L", "N", "P", "H"]
]

def readInput():
	data = []
	with open("Day-5/inputs.txt", "r") as file:
		data = [
			line.strip("\n").replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
			for line in file
		]

	return data

def main():
	procedures = readInput()

	for p in procedures:
		amount = int(p[0])
		fromStack = int(p[1]) - 1
		toStack = int(p[2]) - 1

		stackLen = len(stack[fromStack])
		elements = stack[fromStack][stackLen-amount:stackLen]
		elements = elements[::-1] # reverse
		del stack[fromStack][stackLen-amount:stackLen]
		stack[toStack] += elements

	print("The top elements are:", [i[-1] for i in stack])

main()