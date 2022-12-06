# The start of message marker is 14 distinct characters rather than 4.

def readInput():
	with open("Day-6/inputs.txt", "r") as file:
		return file.read()

def signalReceived(signal, current):
	current.append(signal)
	if len(current) > 14:
		del current[0]

	if len(current) == 14:
		if len(set(current)) == len(current):
			return current, True
	
	return current, False

def main():
	dataStream = readInput()
	current = []
	passes = 0
	found = False

	for signal in dataStream:
		current, found = signalReceived(signal, current)
		passes += 1
		if found:
			break

	print("The start marker was found after:", passes)

main()