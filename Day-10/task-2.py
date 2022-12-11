# Register X controls the horizontal position of a sprite.
# THe sprite is 3 pixels wide, and the X reigster sets the horizontal position of the middle of that sprite.
# There is NO vertical position.
# 40 Pixels wide and 6 high, drawing from left to right each row at a time.
# A single pixel is drawn in a single cycle.
# '#' represents a lit pixel, '.' is a dark pixel.

# Render the Output

def readInputs():
	with open("Day-10/inputs.txt", "r") as file:
		data = [line.strip("\n").split(" ") for line in file]
	return data

def handleTick(tick, register, display):
	strength = 0
	if tick in [20, 60, 100, 140, 180, 220]:
		strength = tick * register

	rowIndex = (tick - 1) // 40
	colIndex = (tick - 1) % 40
	if abs(register - colIndex) <= 1:
		display[rowIndex][colIndex] = "#"
	else:
		display[rowIndex][colIndex] = "."

	return strength, display

def processInstructions(instructions, display):
	total = 0
	tick = 0
	register = 1

	for instruction in instructions:
		match instruction[0]:
			case "noop":
				tick += 1
				strength, display = handleTick(tick, register, display)
				total += strength
			case "addx":
				tick += 1
				strength, display = handleTick(tick, register, display)
				total += strength
				tick += 1
				strength, display = handleTick(tick, register, display)
				total += strength
				register += int(instruction[1])

	return total, display

def main():
	instructions = readInputs()

	# Create the blank display
	display = []
	for row in range(6):
		display.append([])
		for col in range(40):
			display[row].append(".")

	total, display = processInstructions(instructions, display)

	# Output total
	print("The sum is:", total)

	# Output the display
	for row in range(6):
		print("".join(display[row]))

main()