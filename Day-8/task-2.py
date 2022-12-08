# The elves want a tree with the greatest viewing distance.
# To calcualte the viewing distance from a tree, look left, right, up, and down from the tree.
# Stop if you reach an edge or reach a tree with the same height or greater.

# A trees scenic score is found by multiplying together its viewing distance in each four directions.
# Find the highest scenic score.

def readInput():
	data = []
	with open("Day-8/inputs.txt", "r") as file:
		lines = file.read().splitlines()
		data = [list(map(int, line)) for line in lines] # create 2d array of the numbers

	return data

def main():
	data = readInput()
	total = 0

	for rowIndex in range(0, len(data)):
		for treeIndex in range(0, len(data[rowIndex])):
			tree = data[rowIndex][treeIndex]
			# Get all elements around the current tree - Left starts at 0 and goes to current element, Right goes from element to the right to end of row (same for top and bottom)
			allLeft = [data[rowIndex][col] for col in range(0, treeIndex)]
			allLeft = allLeft[::-1] # needs reversing to be in right order
			allRight = [data[rowIndex][col] for col in range(treeIndex+1, len(data[rowIndex]))]
			allTop = [data[row][treeIndex] for row in range(0, rowIndex)]
			allTop = allTop[::-1] # needs reversing to be in right order
			allBottom = [data[row][treeIndex] for row in range(rowIndex+1, len(data))]
			
			# Scores for different directions, used to calculate scenic score
			leftScore = 0
			rightScore = 0
			topScore = 0
			bottomScore = 0

			# loop over each direction and add till a tree larger is hit
			for left in allLeft:
				leftScore += 1
				if left >= tree:
					break
			for right in allRight:
				rightScore += 1
				if right >= tree:
					break
			for top in allTop:
				topScore += 1
				if top >= tree:
					break
			for bottom in allBottom:
				bottomScore += 1
				if bottom >= tree:
					break
			
			# scenic score
			newTotal = leftScore * rightScore * topScore * bottomScore
			if newTotal > total: # if a better scenic score
				total = newTotal

	print("Total trees visible:", total)

main()