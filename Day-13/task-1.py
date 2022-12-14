# Signal is decoded out of order.
# You need to re-order the list of packets, input, to decode the message.
# Your list consists of pairs of packets.
# Pairs are separated by a bank line.
# You need to identify how many pairs of packets are in the right order.

# Packet data consists of lists and integers.
# Each list starts with [ and ends with ]
# It contains zeo or more comma separated values, integers or other lists.

# When comparing two values, the first value is called left and the second value is the right.
# If both values are integers, the lower integer should come first. 
	# If the left is lower than the right, they are in the correct order.
	# If the left is higher than the right, they must be swapped.
# If both values are lists, compare the first value of each list, then the second, so on...
	# If the left list runs out of items first, the inputs are in the correct order.
	# If the right list runs out of items first, the inputs aren't in the correct order.
# if exactly one value is integer, convert the integer to a list which contains that integer.
	# Then do above compare

# Return the sum of the index of each pair that is in the correct order.

import ast

def readInputs():
	with open("Day-13/inputs.txt", "r") as file:
		pairsData = file.read().split("\n\n")
	pairs = []
	for pair in pairsData:
		pair = pair.split("\n")
		pairs.append(pair)
	return pairs

# Return 1 if correct order, return 0 reverable order, return -1 if wrong order
def compare(p1, p2):
	if isinstance(p1, int) and isinstance(p2, list):
		p1 = [p1]
	if isinstance(p1, list) and isinstance(p2, int):
		p2 = [p2]

	if isinstance(p1, int) and isinstance(p2, int):
		if p1 < p2:
			return 1
		if p1 == p2:
			return 0
		if p1 > p2:
			return -1

	if isinstance(p1, list) and isinstance(p2, list):
		index = 0
		minLength = min(len(p1), len(p2))
		while index < minLength:
			val = compare(p1[index], p2[index])

			if val == 1:
				return 1
			if val == -1:
				return -1
			
			index += 1
		
		if index == len(p1):
			if len(p1) == len(p2):
				return 0
			else:
				return 1

		if index == len(p2):
			return -1

def main():
	total = 0

	rawPairs = readInputs()
	pairs = []
	for pair in rawPairs:
		p1 = pair[0]
		p2 = pair[1]
		newPair = [ast.literal_eval(p1), ast.literal_eval(p2)]
		pairs.append(newPair)
	
	index = 1
	for pair in pairs:
		if compare(pair[0], pair[1]) == 1:
			total += index
		index += 1

	print("The sum is:", total)

main()