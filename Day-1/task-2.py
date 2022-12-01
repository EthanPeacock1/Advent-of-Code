# Adapted versi9on of Task 1, but instead finding the total of the top 3 Elves.

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
	calorieArr.sort(reverse=True)
	top3Total = calorieArr[0] + calorieArr[1] + calorieArr[2]
	print("Total of Top 3:", top3Total)

main()