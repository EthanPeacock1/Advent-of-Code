import ast
import functools

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
		pairs.append(ast.literal_eval(p1))
		pairs.append(ast.literal_eval(p2))
	pairs.append([[2]])
	pairs.append([[6]])
	pairs = sorted(pairs, key=functools.cmp_to_key(compare), reverse=True)

	index = 1
	additionalPacket1 = 0
	additionalPacket2 = 0
	for pair in pairs:
		if pair == [[2]]:
			additionalPacket1 = index
		if pair == [[6]]:
			additionalPacket2 = index
		index += 1

	total = additionalPacket1 * additionalPacket2
	print("The sum is:", total)

main()