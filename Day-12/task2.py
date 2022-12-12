# We do not need to start at 'S', but any square that is of elevation 'a'

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

		# because we are backtracking, we start at the highest level and can only move down
		if getHeight(heightMap[newRow][newCol]) >= getHeight(heightMap[row][col]) - 1:
			neighbours.append([newRow, newCol])
	
	return neighbours

def dijkstra(source, end):
	visited = []
	for row in range(len(heightMap)):
		visited.append([])
		for col in range(len(heightMap[0])):
			visited[row].append([False])
	queue = PriorityQueue()

	# We now start at the end and backtrack, because we have multiple possible start locations
	queue.insert((end[0], end[1], 0)) # Tuple of row, col, weight
	minSteps = 0

	while True:
		r, c, weight = queue.delete()

		if visited[r][c] == True:
			continue
		visited[r][c] = True

		# We just need to reach a square that is of height 0, i.e., 'a'
		if getHeight(heightMap[r][c]) == 0:
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