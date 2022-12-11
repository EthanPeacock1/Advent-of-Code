# The device has a screen and simple CPU driven by a precise clock circuit, with each tick called a cycle.
# The CPU has a simple register, X, which starts with the value 1.
# It supports two instructions:
	# addx V - takes two cycles to complete, after which the X register is increased by V
	# noop - takes one cylce, and has no effect.
# The signal strength = cycle number * X value

# Find the sum of the signal strength during the 20th, 60th, 100th, 140th, 180th and 220th cycle.

def readInputs():
	with open("Day-10/inputs.txt", "r") as file:
		data = [line.strip("\n").split(" ") for line in file]
	return data

def strengthCheck(tick, register):
	strength = 0
	if tick in [20, 60, 100, 140, 180, 220]:
		strength = tick * register

	return strength

def processInstructions(instructions):
	total = 0
	tick = 0
	register = 1

	for instruction in instructions:
		match instruction[0]:
			case "noop":
				tick += 1
				total += strengthCheck(tick, register)
			case "addx":
				tick += 1
				total += strengthCheck(tick, register)
				tick += 1
				total += strengthCheck(tick, register)
				register += int(instruction[1])

	return total

def main():
	instructions = readInputs()
	total = processInstructions(instructions)

	# Output total
	print("The sum is:", total)

main()