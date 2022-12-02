# Player 1: A = Rock | B = Paper | C = Scissors
# Required Outcome: X = Lose | Y = Draw | Z = Win

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

	plays = {
		"X": { # Need to Lose
			"A": 3, # Lose (0) + Scissors (3)
			"B": 1, # Lose (0) + Rock (1)
			"C": 2  # Lose (0) + Paper (2)
		},
		"Y": { # Need to Draw
			"A": 4, # Draw (3) + Rock (1)
			"B": 5, # Draw (3) + Paper (2)
			"C": 6  # Draw (3) + Scissors (3)
		},
		"Z": { # Need to Win
			"A": 8, # Win (6) + Paper (2)
			"B": 9, # Win (6) + Scissors (3)
			"C": 7  # Win (6) + Rock (1)
		}
	}

	score = plays[p2][p1]
				
	return score

def main():
	rounds = []
	totalScore = 0

	rounds = readInput()
	for r in rounds:
		totalScore += playRound(r)
	
	print("Total Score was:", totalScore)

main()