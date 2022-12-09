# The rope will now contain 10 knots, 9 excluding the head.
# Now simulate all 9 knots following the head.
# Return the number of positions the end of the rope (10th knot) visits.

def readInput():
	with open("Day-9/inputs.txt", "r") as file:
		data = [line.strip("\n").split(" ") for line in file]
	return data

def processInstruction(headPos, tails, direction, amount):
	for move in range(amount):
		headPos = moveHead(headPos, direction)
		for t in range(0, len(tails)): # loop over every tail and move accordingly to the head/tail in front
			if t == 0:
				infront = headPos
			else:
				infront = tails[t-1]
			tail = tails[t]
			if t < 8:
				newPos = moveTail(infront, tail, False)
			else:
				newPos = moveTail(infront, tail, True) # track how many positions it visits
			tails[t] = newPos

	return headPos, tails

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

def moveTail(infrontPos, behindPos, track):
	xDiff = abs(infrontPos[0] - behindPos[0])
	yDiff = abs(infrontPos[1] - behindPos[1])

	# Move in both directions, for task 2 this can be a gap of 2, e.g.,
	# T = furthest tail, t = inner tail, H = head

	#          (R 1)       (update t)      (update T)
	# T . . .        T . . .        T . . .        . . . .
	# . t . .   ->   . t . .   ->   . . . .   ->   . T . .
	# . . H .        . . . H        . . t H        . . t H
	if ((xDiff == 2) and (yDiff == 1)) or ((xDiff == 1) and (yDiff == 2)) or ((xDiff == 2) and (yDiff == 2)):
		if infrontPos[0] > behindPos[0]:
			behindPos[0] += 1
		else:
			behindPos[0] -= 1
		if infrontPos[1] > behindPos[1]:
			behindPos[1] += 1
		else:
			behindPos[1] -= 1
		if track and not hasVisited(behindPos):
			visited.append([behindPos[0], behindPos[1]])
	elif (xDiff > 1) and (yDiff < 2): # move in x value
		if infrontPos[0] > behindPos[0]:
			behindPos[0] += 1
		else:
			behindPos[0] -= 1
		if track and not hasVisited(behindPos):
			visited.append([behindPos[0], behindPos[1]])
	elif (xDiff < 2) and (yDiff > 1): # move in y value
		if infrontPos[1] > behindPos[1]:
			behindPos[1] += 1
		else:
			behindPos[1] -= 1
		if track and not hasVisited(behindPos):
			visited.append([behindPos[0], behindPos[1]])
	
	return behindPos

def main():
	instructions = readInput()
	headPos = [0, 0] # x and y (row position, column position)
	tails = [[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0],[0, 0]]
	for instruction in instructions:
		headPos, tails = processInstruction(headPos, tails, instruction[0], int(instruction[1]))

	print("Total positions visited:", len(visited))

main()