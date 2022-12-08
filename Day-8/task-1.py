# Evles encounter some tall trees and wonder if it's a good location for a tree house.
# First, determine whether there is enough tree cover to keep the tree house hideen.
# each number of the input string is the trees height, 0 being the shortest and 9 the tallest.

# A tree is visible if all the other trees between it and an edge of te grid are shorter than it.
# All the trees around the edge of the grid are visible.

def readInput():
	data = []
	with open("Day-8/inputs.txt", "r") as file:
		lines = file.read().splitlines()
		data = [list(map(int, line)) for line in lines] # create 2d array of the numbers

	return data

def main():
	data = readInput()
	total = 0

	# Pre-add the outside grid elements
	outsideRow = len(data[0]) * 2
	outsideColumn = (len(data) - 2) * 2
	total += outsideRow
	total += outsideColumn

	# Start at index 1, outside elements are ignored and already added
	for rowIndex in range(1, len(data)-1):
		for treeIndex in range(1, len(data[rowIndex])-1):
			tree = data[rowIndex][treeIndex]
			# Get all elements around the current tree - Left starts at 0 and goes to current element, Right goes from element to the right to end of row (same for top and bottom)
			allLeft = [data[rowIndex][col] for col in range(0, treeIndex)]
			allRight = [data[rowIndex][col] for col in range(treeIndex+1, len(data[rowIndex]))]
			allTop = [data[row][treeIndex] for row in range(0, rowIndex)]
			allBottom = [data[row][treeIndex] for row in range(rowIndex+1, len(data))]

			# if the biggest element of anything in a direction is smaller than the current tree, is it visible so add 1
			if tree > max(allLeft) or tree > max(allRight) or tree > max(allTop) or tree > max(allBottom):
				total += 1

	print("Total trees visible:", total)

main()