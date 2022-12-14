rocks = set()

def readInputs():
	with open("Day-14/inputs.txt", "r") as file:
		data = file.read().splitlines()
	return data

def debug(coords):
	global rocks
	smallestX = min([c[0] for c in coords])
	biggestX = max([c[0] for c in coords]) + 1
	smallestY = min([c[1] for c in coords])
	biggestY = max([c[1] for c in coords]) + 1

	output = "\n"
	for y in range(smallestY, biggestY):
		for x in range(smallestX, biggestX):
			currentCoord = (x, y)
			if currentCoord in rocks:
				output += "# "
			else:
				output += ". "
		output += "\n"

	print(output)

def createRocks(raw):
	global rocks
	for line in raw:
		coords = []
		for stringCoord in line.split(" -> "):
			stringX, stringY = stringCoord.split(",")
			x, y = int(stringX), int(stringY)
			coords.append((x, y))

		# For every coord generated from above, compared to previous
		for coord in range(1, len(coords)):
			x = coords[coord][0]
			y = coords[coord][1]
			px = coords[coord-1][0]
			py = coords[coord-1][1]

			# If x XOR y is different, generate the gaps

			if y != py and x == px:
				for ny in range(min(y, py), max(y, py) + 1):
					rocks.add((x, ny))
			
			if x != px and y == py:
				for nx in range(min(x, px), max(x, px) + 1):
					rocks.add((nx, y))
		
	debug(coords)

def dropSand(biggestY):
	global rocks
	currentX = 500
	currentY = 0

	while currentY <= biggestY:
		# down
		if (currentX, currentY + 1) not in rocks:
			currentY += 1
			continue
		# left
		if (currentX - 1, currentY + 1) not in rocks:
			currentX -= 1
			currentY += 1
			continue
		# right
		if (currentX + 1, currentY + 1) not in rocks:
			currentX += 1
			currentY += 1
			continue

		rocks.add((currentX, currentY))

		return True # continue
	return False # end

def main():
	global rocks
	raw = readInputs()
	createRocks(raw)
	biggestY = max([c[1] for c in rocks])
	total = 0

	while True:
		contin = dropSand(biggestY)
		if contin == False:
			break
		total += 1
	
	print("total:", total)

main()