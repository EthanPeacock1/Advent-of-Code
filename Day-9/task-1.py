# The head and tail of the rope must always be touching.
# This mans the tail must be above, next to, or diagonal to the head.
# The head is given a number of instructions on where to move.
# The head and tail start on the same position.

# Return the number of positions the tail visited at least once.
# The starting position does count as a visited for the tail.

def readInput():
	with open("Day-9/inputs.txt", "r") as file:
		data = [line.strip("\n").split(" ") for line in file]
	return data

def processInstruction(headPos, tailPos, direction, amount):
	for move in range(amount):
		headPos = moveHead(headPos, direction)
		tailPos = moveTail(headPos, tailPos)

	return headPos, tailPos

def moveHead(headPos, direction):
	newPos = []
	match direction:
		case "L": # left
			newPos = [headPos[0]-1, headPos[1]]
		case "R": # right
			newPos = [headPos[0]+1, headPos[1]]
		case "U": # up
			newPos = [headPos[0], headPos[1]+1]
		case "D": # down
			newPos = [headPos[0], headPos[1]-1]

	return newPos

visited = [[0, 0]]
def hasVisited(pos):
	if pos in visited:
		return True
	else:
		return False

def moveTail(headPos, tailPos):
	# Get the difference between the 2 given points
	xDiff = abs(headPos[0] - tailPos[0])
	yDiff = abs(headPos[1] - tailPos[1])

	if ((xDiff == 2) and (yDiff == 1)) or ((xDiff == 1) and (yDiff == 2)): # move in both directions (diagonal)
		if headPos[0] > tailPos[0]: # move positive
			tailPos[0] += 1
		else: # move negative
			tailPos[0] -= 1
		if headPos[1] > tailPos[1]: # move positive
			tailPos[1] += 1
		else: # move negative
			tailPos[1] -= 1
		if not hasVisited(tailPos):
			visited.append([tailPos[0], tailPos[1]])
	elif (xDiff > 1) and (yDiff < 2): # move in x value
		if headPos[0] > tailPos[0]: # move positive
			tailPos[0] += 1
		else: # move negative
			tailPos[0] -= 1
		if not hasVisited(tailPos):
			visited.append([tailPos[0], tailPos[1]])
	elif (xDiff < 2) and (yDiff > 1): # move in y value
		if headPos[1] > tailPos[1]: # move positive
			tailPos[1] += 1
		else: # move negative
			tailPos[1] -= 1
		if not hasVisited(tailPos):
			visited.append([tailPos[0], tailPos[1]])
	
	return tailPos

def main():
	instructions = readInput()
	headPos = tailPos = [0, 0] # x and y (row position, column position)
	for instruction in instructions:
		headPos, tailPos = processInstruction(headPos, tailPos, instruction[0], int(instruction[1]))

	print("Total positions visited:", len(visited))

main()