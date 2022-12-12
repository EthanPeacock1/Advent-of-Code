# The puzzle input is a heighthamp from above
# 'a' is the lowest, 'z' is the highest
# Included is your start location, 'S', and desired end position, 'E'.
# The desired location is of 'z' height
# Each move can be one step either up, down, left or right
# You can only step up by 1, for example 'b' -> 'c' is valid, 'b' -> 'd' is not

# Return the fewest steps from the start location to the end

import string
from priorityQueue import PriorityQueue

heightMap = []

def readInputs():
	with open("Day-12/inputs.txt", "r") as file:
		lines = file.read().splitlines()
	data = [list(line) for line in lines]
	return data

def getHeight(stringVal):
	# Use ascii indexes to translate the letter into a height number
	if stringVal in string.ascii_lowercase:
		return string.ascii_lowercase.index(stringVal)
	elif stringVal == "S":
		return 0
	elif stringVal == "E":
		return 25

def getNeighbours(row, col):
	moves = [[1, 0], [-1, 0], [0, -1], [0, 1]]
	neighbours = []
	for dr, dc in moves:
		newRow = row + dr
		newCol = col + dc

		# check whether this is within the grid
		if not (0 <= newRow < len(heightMap) and 0 <= newCol < len(heightMap[0])):
			continue

		# can't move to a square that is more than 1 taller than the current square
		if getHeight(heightMap[newRow][newCol]) <= getHeight(heightMap[row][col]) + 1:
			neighbours.append([newRow, newCol])
	
	return neighbours

def dijkstra(source, end):
	visited = []
	for row in range(len(heightMap)):
		visited.append([])
		for col in range(len(heightMap[0])):
			visited[row].append([False])
	queue = PriorityQueue()

	queue.insert((source[0], source[1], 0)) # Tuple of row, col, weight
	minSteps = 0

	while True:
		r, c, weight = queue.delete()

		if visited[r][c] == True:
			continue
		visited[r][c] = True

		if [r, c] == end:
			minSteps = weight
			break

		for newRow, newCol in getNeighbours(r, c):
			queue.insert((newRow, newCol, weight + 1))

	return minSteps

def main():
	global heightMap
	heightMap = readInputs()
	
	# Find start and end positions
	startIndex = []
	endIndex = []
	for rowIndex in range(len(heightMap)):
		row = heightMap[rowIndex]
		if "S" in row:
			startIndex = [rowIndex, row.index("S")]
		if "E" in row:
			endIndex = [rowIndex, row.index("E")]
	
	minimumSteps = dijkstra(startIndex, endIndex)
	print("The minimum steps was:", minimumSteps)

main()