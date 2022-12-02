# Player 1: A = Rock | B = Paper | C = Scissors
# Player 2: X = Rock | Y = Paper | Z = Scissors

# Round Score = Shape selected + Outcome
# Shape Scores = 1 for Rock, 2 for Paper and 3 for Scissors
# Outcome Scores = 0 if lost, 3 if draw and 6 if win.

# Total Score is the sum of every Rounds Score.

def readInput():
	rounds = []

	with open("Day-2/inputs.txt") as file:
		for line in file:
			newRound = line.strip("\n").split(" ")
			rounds.append(newRound)

	return rounds

def playRound(inputs):
	p1 = inputs[0] # elf
	p2 = inputs[1] # me
	score = 0

	match p2:
		case "X": # Rock
			score += 1
			if p1 == "A": # Rock
				score += 3
			elif p1 == "B": # Paper
				score += 0
			else: # Scissors
				score += 6
		case "Y": # Paper
			score += 2
			if p1 == "A": # Rock
				score += 6
			elif p1 == "B": # Paper
				score += 3
			else: # Scissors
				score += 0
		case "Z": # Scissors
			score += 3
			if p1 == "A": # Rock
				score += 0
			elif p1 == "B": # Paper
				score += 6
			else: # Scissors
				score += 3

	return score

def main():
	rounds = []
	totalScore = 0

	rounds = readInput()
	for r in rounds:
		totalScore += playRound(r)
	
	print("Total Score was:", totalScore)

main()