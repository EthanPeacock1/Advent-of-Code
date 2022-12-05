# Stacks of crates can now be moved.

# Non-hard coded version of stack.
def readInput():
	with open("Day-5/inputs.txt", "r") as file:
		data, instrucs = file.read().split("\n\n")
	
	# Creating Stack
	stacks = [[], [], [], [], [], [], [], [], []]
	data = data[::-1]
	data = data.split("\n")
	for row in data[1:]:
		stackIndex = 8
		for crate in range(1, len(row), 4):
			if row[crate] != " ":
				stacks[stackIndex].append(row[crate])
			stackIndex -= 1

	moves =	[
		line.strip("\n").replace("move ", "").replace("from ", "").replace("to ", "").split(" ")
		for line in instrucs.split("\n")
	]

	return stacks, moves

def main():
	stacks, procedures = readInput()

	for p in procedures:
		amount = int(p[0])
		fromStack = int(p[1]) - 1
		toStack = int(p[2]) - 1

		stackLen = len(stacks[fromStack])
		elements = stacks[fromStack][stackLen-amount:stackLen]
		del stacks[fromStack][stackLen-amount:stackLen]
		stacks[toStack] += elements

	print("The top elements are:", [i[-1] for i in stacks])

main()