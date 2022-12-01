# Calculate the Elf with the most Calories.
# The Elf will be carrying food, Elves are split by an empty line.

def readInputs():
	totaledCalories = []
	elfTotal = 0
	with open("Day-1/inputs.txt", "r") as file:
		for line in file:
			if line == "\n":
				totaledCalories.append(elfTotal)
				elfTotal = 0
			else:
				elfTotal += int(line)

	return totaledCalories

def main():
	calorieArr = readInputs()
	calorieArr.sort()
	print("Largest:", calorieArr[-1])

main()